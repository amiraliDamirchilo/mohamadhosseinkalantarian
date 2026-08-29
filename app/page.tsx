'use client';

import { useState } from 'react';

const services = [
  ['Architectural BIM Modeling', 'Accurate Revit models developed from architectural drawings, design intent, and construction requirements.'],
  ['Point Cloud to BIM', 'Precise as-built Revit models created from point-cloud scans for renovation and documentation projects.'],
  ['Custom Revit Families', 'Clean, parametric families made for project-specific architectural elements and components.'],
];

const projects = [
  {
    title: 'Ravia Villa', image: '/ravia-villa.jpg', alt: 'BIM details and exterior views of Ravia Villa',
    architect: 'Ahmad Saffar', scope: 'BIM modeling and detail development',
    text: 'A two-story villa translated from architectural design into a detailed, practical Revit model. My work covered interior details, the façade, and its technical connections.',
  },
  {
    title: 'Qeshm Vernacular Villa', image: '/qeshm-villa.jpg', alt: 'Qeshm Vernacular Villa',
    architect: 'Mohammad Hassan Forouzanfar', scope: 'BIM, documentation, and coordination',
    text: 'A contemporary vernacular villa inspired by Qeshm Island’s climate, local materials, and traditions. My role covered BIM modeling, architectural detailing, and construction documentation.',
  },
];

export default function Home() {
  const [menuOpen, setMenuOpen] = useState(false);

  return (
    <main>
      <header className="header">
        <a href="#top" className="logo">Mohamad Kalantarian</a>
        <button className="menu" type="button" aria-expanded={menuOpen} onClick={() => setMenuOpen(!menuOpen)}>
          {menuOpen ? 'Close' : 'Menu'}
        </button>
        <nav className={menuOpen ? 'nav open' : 'nav'}>
          <a href="#services" onClick={() => setMenuOpen(false)}>Services</a>
          <a href="#work" onClick={() => setMenuOpen(false)}>Work</a>
          <a href="#contact" onClick={() => setMenuOpen(false)}>Contact</a>
        </nav>
      </header>

      <section className="hero" id="top">
        <div className="hero-copy">
          <p className="label">BIM Specialist · Revit Modeler</p>
          <h1>Clear models.<br />Accurate outcomes.</h1>
          <p className="intro">I help architects and AEC teams turn drawings, designs, and point clouds into accurate Revit BIM models.</p>
          <a className="link" href="mailto:mh.kalantaryan@gmail.com">Start a project ↗</a>
        </div>
        <img className="hero-image" src="/mohamad-portrait-01.jpg" alt="Mohamad Kalantarian" />
      </section>

      <section className="section" id="services">
        <div className="section-title">
          <p className="label">01 / Services</p>
          <h2>What I do</h2>
        </div>
        <div className="service-list">
          {services.map((service, index) => (
            <article className="service" key={service[0]}>
              <span>0{index + 1}</span><h3>{service[0]}</h3><p>{service[1]}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="section" id="work">
        <div className="section-title">
          <p className="label">02 / Selected work</p>
          <h2>Projects</h2>
        </div>
        <div className="projects">
          {projects.map((project, index) => (
            <article className="project" key={project.title}>
              <img src={project.image} alt={project.alt} />
              <div className="project-copy">
                <span className="project-index">0{index + 1}</span>
                <h3>{project.title}</h3>
                <p>{project.text}</p>
                <dl>
                  <div><dt>Architect</dt><dd>{project.architect}</dd></div>
                  <div><dt>Scope</dt><dd>{project.scope}</dd></div>
                </dl>
              </div>
            </article>
          ))}
        </div>
      </section>

      <section className="about section">
        <div className="section-title">
          <p className="label">03 / About</p>
          <h2>Mohamad<br />Kalantarian</h2>
        </div>
        <div className="about-content">
          <img src="/mohamad-portrait-02.jpg" alt="Mohamad Kalantarian, BIM specialist" />
          <p>I work with architects and AEC teams to create reliable Revit models with a focus on clarity, coordination, and buildable detail.</p>
        </div>
      </section>

      <footer className="footer" id="contact">
        <p className="label">Have a project in mind?</p>
        <h2>Let’s work together.</h2>
        <a className="footer-email" href="mailto:mh.kalantaryan@gmail.com">mh.kalantaryan@gmail.com ↗</a>
        <div className="footer-bottom">
          <p>Mohamad Kalantarian<br /><span>BIM Specialist · Revit Modeler</span></p>
          <div className="socials">
            <a href="https://t.me/mh_kalantaryan" target="_blank" rel="noreferrer">Telegram ↗</a>
            <a href="https://www.instagram.com/mh.kalantrayan" target="_blank" rel="noreferrer">Instagram ↗</a>
            <a href="https://www.linkedin.com/in/mohammad-kalantaryan-baa896397" target="_blank" rel="noreferrer">LinkedIn ↗</a>
          </div>
        </div>
      </footer>
    </main>
  );
}
