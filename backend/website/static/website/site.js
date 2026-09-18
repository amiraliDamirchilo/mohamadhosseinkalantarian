(() => {
  const $ = (selector) => document.querySelector(selector);
  const make = (tag, className, value) => {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (value !== undefined) node.textContent = value;
    return node;
  };
  const imageUrl = (path) => path && path.startsWith('/') && !path.startsWith('/static/') ? `/static${path}` : path;
  const menu = $('.menu');
  menu.addEventListener('click', () => {
    const open = $('.nav').classList.toggle('open');
    menu.textContent = open ? 'Close' : 'Menu';
    menu.setAttribute('aria-expanded', String(open));
  });
  document.querySelectorAll('.nav a').forEach(link => link.addEventListener('click', () => {
    $('.nav').classList.remove('open'); menu.textContent = 'Menu'; menu.setAttribute('aria-expanded', 'false');
  }));

  let content = {};
  let projects = [];
  let activeCategory = '';

  const renderProjects = () => {
    const list = $('#projects-list');
    const subset = activeCategory ? projects.filter(project => project.category === activeCategory) : projects;
    if (!subset.length) return;
    list.replaceChildren();
    subset.forEach((project, index) => {
      const article = make('article', 'project');
      const image = make('img'); image.src = imageUrl(project.image); image.alt = project.image_alt || project.title; article.append(image);
      const copy = make('div', 'project-copy');
      copy.append(make('span', 'project-index', String(index + 1).padStart(2, '0')), make('h3', '', project.title), make('p', '', project.description));
      const details = make('dl');
      [[content.architect_label || 'Architect', project.architect], [content.scope_label || 'Scope', project.scope]].forEach(([label, value]) => {
        const row = make('div'); row.append(make('dt', '', label), make('dd', '', value)); details.append(row);
      });
      copy.append(details);
      if (project.media && project.media.length) {
        const gallery = make('div', 'media-gallery');
        project.media.forEach(media => {
          const figure = make('figure');
          const asset = make(media.type === 'video' ? 'video' : 'img');
          asset.src = imageUrl(media.url); asset.alt = media.alt || project.title;
          if (media.type === 'video') { asset.controls = true; asset.preload = 'metadata'; }
          figure.append(asset);
          if (media.caption) figure.append(make('figcaption', '', media.caption));
          gallery.append(figure);
        });
        copy.append(gallery);
      }
      article.append(copy); list.append(article);
    });
  };

  const renderCategories = (categories) => {
    const filter = $('#category-filter');
    if (!categories.length) return;
    filter.hidden = false; filter.replaceChildren();
    const addButton = (label, slug) => {
      const button = make('button', !slug ? 'active' : '', label); button.type = 'button';
      button.addEventListener('click', () => { activeCategory = slug; filter.querySelectorAll('button').forEach(item => item.classList.toggle('active', item === button)); renderProjects(); });
      filter.append(button);
    };
    addButton('All', ''); categories.forEach(category => addButton(category.name, category.slug));
  };

  Promise.all([fetch('/api/content/'), fetch('/api/services/'), fetch('/api/portfolio/categories/'), fetch('/api/portfolio/projects/')])
    .then(async responses => {
      if (responses.some(response => !response.ok)) throw new Error('API unavailable');
      return Promise.all(responses.map(response => response.json()));
    })
    .then(([text, services, categories, apiProjects]) => {
      content = text;
      document.querySelectorAll('[data-content]').forEach(element => {
        const value = content[element.dataset.content];
        if (value) element.textContent = value;
      });
      document.querySelectorAll('[data-mailto]').forEach(element => { element.href = `mailto:${content.email || 'mh.kalantaryan@gmail.com'}`; });
      const serviceList = $('#services-list');
      if (services.length) {
        serviceList.replaceChildren();
        services.forEach((service, index) => {
          const item = make('article', 'service'); item.append(make('span', '', String(index + 1).padStart(2, '0')), make('h3', '', service.title), make('p', '', service.description)); serviceList.append(item);
        });
      }
      projects = apiProjects; renderCategories(categories); renderProjects();
    })
    .catch(() => { /* The server-rendered fallback remains visible if the API is unavailable. */ });
})();
