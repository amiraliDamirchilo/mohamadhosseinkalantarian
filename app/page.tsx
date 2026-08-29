'use client';

import { useState } from 'react';

const services = [
  {
    number: '01',
    title: 'BIM Modeler — Architecture',
    description:
      'Accurate, construction-ready Revit models developed from architectural drawings and design intent, with close attention to every interface and detail.',
    meta: 'DRAWINGS → COORDINATED BIM',
  },
  {
    number: '02',
    title: 'Point Cloud to BIM',
    description:
      'Precise digital reconstruction of existing buildings from laser-scan point clouds—built for renovation, documentation, and informed design decisions.',
    meta: 'SCAN DATA → REVIT MODEL',
  },
  {
    number: '03',
    title: 'Custom Revit Families',
    description:
      'Purpose-built parametric families for project-specific elements, from custom cabinetry to architectural components, made to perform cleanly inside your model.',
    meta: 'UNIQUE ELEMENTS → SMART OBJECTS',
  },
];

const projects = [
  {
    number: '01',
    title: 'Ravia Villa',
    subtitle: 'From BIM to Reality',
    image: '/ravia-villa.jpg',
    alt: 'Facade details and exterior views of the two-story Ravia Villa',
    architect: 'Ahmad Saffar',
    scope: 'BIM Modeling · Detail Development',
    description:
      'A two-story villa where I worked as the BIM specialist, translating the architectural design into a detailed, practical Revit model. My work covered the full set of implementation details—from interior elements to the façade and its technical connections.',
  },
  {
    number: '02',
    title: 'Qeshm Vernacular Villa',
    subtitle: 'BIM & Detail Development',
    image: '/qeshm-villa.jpg',
    alt: 'Contemporary vernacular villa in Qeshm Island',
    architect: 'Mohammad Hassan Forouzanfar',
    scope: 'BIM · Documentation · Coordination',
    description:
      'A contemporary vernacular villa on Qeshm Island, inspired by the region’s climate, materials, and architectural traditions. I led BIM modeling, architectural detailing, construction documentation, and coordination between architectural and structural systems.',
  },
];

export default function Home() {
  const [menuOpen, setMenuOpen] = useState(false);
  const closeMenu = () => setMenuOpen(false);

  return (
    <main>
      <header className="site-header">
        <a className="wordmark" href="#top" aria-label="Mohamad Kalantarian — home">
          <span>MK</span>
          <span className="wordmark-name">Mohamad Kalantarian</span>
        </a>

        <button
          className="menu-button"
          type="button"
          aria-expanded={menuOpen}
          aria-controls="primary-navigation"
          onClick={() => setMenuOpen((open) => !open)}
        >
          {menuOpen ? 'Close' : 'Menu'}
        </button>

        <nav
          id="primary-navigation"
          className={menuOpen ? 'primary-nav is-open' : 'primary-nav'}
          aria-label="Primary navigation"
        >
          <a href="#services" onClick={closeMenu}>Services</a>
          <a href="#work" onClick={closeMenu}>Selected work</a>
          <a href="#about" onClick={closeMenu}>About</a>
          <a className="nav-contact" href="#contact" onClick={closeMenu}>Start a project ↗</a>
        </nav>
      </header>

      <section className="hero" id="top">
        <div className="hero-copy">
          <p className="eyebrow">BIM Specialist · Revit Modeler</p>
          <h1>
            Precision<br />
            <span>built in.</span>
          </h1>
          <p className="hero-statement">
            I help architects &amp; AEC teams turn drawings, designs &amp; point clouds into accurate Revit BIM models.
          </p>
          <div className="hero-actions">
            <a className="button button-dark" href="#work">View selected work <span>↓</span></a>
            <a className="text-link" href="mailto:mh.kalantaryan@gmail.com">Discuss a project ↗</a>
          </div>
        </div>

        <figure className="hero-image-wrap">
          <img
            className="hero-image"
            src="/mohamad-portrait-01.jpg"
            alt="Portrait of Mohamad Kalantarian"
          />
          <figcaption>
            <span>Based in Iran</span>
            <span>Working worldwide</span>
          </figcaption>
        </figure>

        <div className="hero-index" aria-hidden="true">01 — 04</div>
      </section>

      <section className="statement section-pad">
        <p className="section-label">What I do</p>
        <p className="statement-copy">
          I bridge the gap between <em>design intent</em> and buildable reality—creating intelligent BIM models that make complexity clear.
        </p>
      </section>

      <section className="services section-pad" id="services">
        <div className="section-heading">
          <p className="section-label">Services / 03</p>
          <h2>Expertise</h2>
        </div>
        <div className="service-list">
          {services.map((service) => (
            <article className="service-item" key={service.number}>
              <p className="service-number">{service.number}</p>
              <h3>{service.title}</h3>
              <p className="service-description">{service.description}</p>
              <p className="service-meta">{service.meta}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="work section-pad" id="work">
        <div className="section-heading work-heading">
          <p className="section-label">Selected work / 02</p>
          <h2>Projects</h2>
          <p className="heading-note">Detailed models.<br />Precise outcomes.</p>
        </div>

        <div className="project-list">
          {projects.map((project) => (
            <article className="project" key={project.number}>
              <div className="project-image-wrap">
                <img src={project.image} alt={project.alt} />
                <span className="project-number">{project.number}</span>
              </div>
              <div className="project-info">
                <div>
                  <p className="project-kicker">{project.subtitle}</p>
                  <h3>{project.title}</h3>
                </div>
                <p className="project-description">{project.description}</p>
                <dl className="project-meta">
                  <div><dt>Architect</dt><dd>{project.architect}</dd></div>
                  <div><dt>Scope</dt><dd>{project.scope}</dd></div>
                </dl>
              </div>
            </article>
          ))}
        </div>
      </section>

      <section className="about" id="about">
        <div className="about-image-wrap">
          <img src="/mohamad-portrait-02.jpg" alt="Mohamad Kalantarian, BIM specialist" />
        </div>
        <div className="about-copy">
          <p className="section-label light-label">About</p>
          <h2>Mohamad<br />Kalantarian</h2>
          <p className="about-lead">
            BIM specialist focused on architectural precision, technical clarity, and models that work beyond the screen.
          </p>
          <p className="about-body">
            I collaborate with architects and AEC teams to turn early design information, drawing sets, and site scans into reliable Revit models. Every deliverable is developed with construction logic, coordination, and the final built result in mind.
          </p>
          <a className="button button-light" href="#contact">Work with me <span>↗</span></a>
        </div>
      </section>

      <footer className="contact section-pad" id="contact">
        <div className="contact-top">
          <p className="section-label light-label">Have a project in mind?</p>
          <h2>Let’s build it<br /><span>accurately.</span></h2>
        </div>

        <a className="email-link" href="mailto:mh.kalantaryan@gmail.com">
          mh.kalantaryan@gmail.com <span>↗</span>
        </a>

        <div className="footer-grid">
          <div className="footer-signature">
            <p>Mohamad Kalantarian</p>
            <span>BIM Specialist · Revit Modeler</span>
          </div>
          <div className="social-links">
            <a href="https://t.me/mh_kalantaryan" target="_blank" rel="noreferrer">Telegram <span>↗</span></a>
            <a href="https://www.instagram.com/mh.kalantrayan" target="_blank" rel="noreferrer">Instagram <span>↗</span></a>
            <a href="https://www.linkedin.com/in/mohammad-kalantaryan-baa896397" target="_blank" rel="noreferrer">LinkedIn <span>↗</span></a>
          </div>
          <div className="footer-note">
            <p>Available for selected freelance<br />and collaborative BIM projects.</p>
            <span>© {new Date().getFullYear()}</span>
          </div>
        </div>
      </footer>
    </main>
  );
}
