#!/usr/bin/env python3
"""Assemble wave-case-study/index.html hub from backup branding + spec."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
bak = (ROOT / "index.html.bak").read_text()
out_path = ROOT / "index.html"

def extract_between(html, start_marker, end_marker):
    i = html.index(start_marker)
    j = html.index(end_marker, i)
    return html[i:j]

def panel_inner(html, panel):
    pat = rf'<div class="tab-panel(?: active)?" data-panel="{panel}">\s*(.*?)\s*</div>\s*(?=\n<!--|\n<div class="tab-panel"|\n<footer>)'
    m = re.search(pat, html, re.S)
    if not m and panel == "progress":
        m = re.search(r'<div class="tab-panel" data-panel="progress">\s*(.*?)\s*</div>\s*\n<footer>', html, re.S)
    return m.group(1).strip() if m else ""

style = extract_between(bak, "<style>", "</style>")
head = bak.split("<body>")[0] + "<body>\n"

HUB_CSS = """
.hub-lead{
  font-family:'Poppins',sans-serif; font-weight:600; font-size:22px; line-height:1.4;
  color:var(--ink); max-width:640px; margin-top:18px; text-wrap:balance;
}
.hub-cards{
  display:grid; grid-template-columns:repeat(3,1fr); gap:20px; margin-top:28px;
  max-width:1240px;
}
@media (max-width:860px){
  .hub-cards{grid-template-columns:1fr;}
}
.hub-card{
  display:flex; flex-direction:column; align-items:stretch; text-align:left;
  border:1.5px solid var(--line); border-radius:22px; background:var(--paper);
  padding:0; cursor:pointer; font-family:inherit; color:inherit;
  min-height:0; height:auto;
  transition:transform .25s ease, border-color .25s ease, box-shadow .25s ease;
  box-shadow:0 12px 28px -18px #33454A44;
}
.hub-card:hover{transform:translateY(-4px);}
.hub-card[aria-pressed="true"]{
  border-color:var(--coral);
  transform:translateY(-6px);
  box-shadow:0 20px 36px -16px #33454A55, 0 0 0 1px #F2665A33;
}
.hub-card:focus-visible{outline:2px solid var(--coral); outline-offset:3px;}
.hub-card-thumb{
  aspect-ratio:4/3; display:flex; align-items:center; justify-content:center;
  border-bottom:1px solid var(--line); padding:16px;
}
.hub-card-thumb .placeholder-note{padding:0 8px;}
.hub-card-thumb--brand{background:linear-gradient(160deg,#241E4E,#5B4B9A);}
.hub-card-thumb--brand .placeholder-note{color:#C7C0E8;}
.hub-card-thumb--commerce{background:linear-gradient(135deg,#F0A8C4,#7FA8D9);}
.hub-card-thumb--commerce .placeholder-note{color:#33454A;}
.hub-card-thumb--epro{background:linear-gradient(160deg,#478383,#241E4E);}
.hub-card-thumb--epro .placeholder-note{color:#C7C0E8;}
@media (max-width:860px){
  .hub-card-thumb{aspect-ratio:16/8;}
}
.hub-card-body{
  height:128px; box-sizing:border-box; padding:16px 18px 18px;
  display:flex; flex-direction:column; gap:8px;
}
@media (max-width:860px){
  .hub-card-body{height:auto; min-height:128px;}
}
.hub-card-head{
  display:flex; align-items:flex-start; justify-content:space-between; gap:10px;
}
.hub-card-head h3{
  font-family:'Poppins',sans-serif; font-weight:600; font-size:18px; line-height:1.25;
  margin:0; max-width:none; color:var(--teal);
}
.hub-card-selected{
  font-size:11px; font-weight:700; color:var(--coral); text-transform:uppercase;
  letter-spacing:0.04em; flex-shrink:0; visibility:hidden; line-height:1.4;
}
.hub-card[aria-pressed="true"] .hub-card-selected{visibility:visible;}
.hub-card-desc{
  font-size:14px; line-height:1.5; color:var(--ink-soft); margin:0; max-width:none;
  display:-webkit-box; -webkit-line-clamp:3; -webkit-box-orient:vertical; overflow:hidden;
}
.tab-content-set{display:none;}
.tab-content-set.active{display:block;}
#tabSection .tab-nav-anchor{margin-top:8px;}
"""

style = style.replace("</style>", HUB_CSS + "\n</style>", 1)

CHALLENGE_SOLUTION = """
  <div class="block" style="margin-bottom:32px;">
    <div class="section-eyebrow">The Challenge</div>
    <p>WAVE is a medical device designed to relieve menstrual pain, with a clinical study currently being planned to secure FDA clearance. WAVE is a device with real clinical credibility, but its brand undermined it.</p>
    <p>Packaging, marketing, and digital presence were inconsistent, eroding trust at the exact moment the product needed to earn it.</p>
    <p>The deeper challenge: repositioning a medical device to present as human and empowering as the best consumer wellness brands, without sacrificing clinical authority.</p>
    <div class="section-eyebrow" style="margin-top:20px;">The Solution</div>
    <p>A full brand system redesign built around "warm authority", the strategic middle ground between clinical coldness and wellness softness. New logo, visual identity, color and typography system, packaging, messaging framework, and social media direction.</p>
    <p style="margin-bottom:0;">Delivered as a complete, handoff-ready brand system that became the foundation for the website and all marketing going forward.</p>
  </div>
"""

br_overview = CHALLENGE_SOLUTION + panel_inner(bak, "overview")
br_design = panel_inner(bak, "design")
br_outcome = panel_inner(bak, "outcome")
br_progress = """<div class="block"><p style="margin-bottom:0;">WAVE is an active client engagement. As Creative Director, I continue to shape the brand across new products and touchpoints.</p></div>"""

# E-Commerce panels (from wave-ecommerce-cursor-prompt structure; ws2 design content from live backup)
ECO_OVERVIEW = """
  <div class="block">
    <div class="section-eyebrow">The Challenge</div>
    <p>WAVE needed a direct-to-consumer sales channel of its own, one that could reflect the brand and handle its specific order and shipping needs, rather than relying on an off-the-shelf platform.</p>
    <div class="section-eyebrow" style="margin-top:20px;">The Approach</div>
    <p style="margin-bottom:0;">Building a custom storefront and admin backend, covering the full customer purchase flow alongside order, buyer, and shipping management, ready to launch once trials allow a sale.</p>
  </div>
  <div class="block">
    <div class="gallery-item wide">[IMG: storefront home page, desktop]</div>
  </div>
"""

ws2 = extract_between(bak, '<div class="ws2-layout">', '</div>\n    </div>\n  </div>\n\n  <div class="block">\n    <div class="section-eyebrow">Workstream 2</div>')
ECO_DESIGN = f"""
  <div class="block">
    <div class="subproject">
      <span class="subproject-tag">Website &amp; E-Commerce</span>
      <div class="ws2-layout">
{ws2}
      </div>
    </div>
  </div>
  <div class="block">
    <div class="gallery">
      <div class="gallery-item">[IMG: clinician resource hub landing page]</div>
      <div class="gallery-item">[IMG: guest checkout flow, key step]</div>
    </div>
  </div>
  <div class="block">
    <div class="gallery-item wide">[PLACEHOLDER: admin order and serial/lot inventory views]</div>
  </div>
"""

ECO_OUTCOME = """
  <div class="block">
    <div class="gallery-item wide">[PLACEHOLDER: launch readiness and fulfillment workflow outcomes]</div>
  </div>
"""

ECO_PROGRESS = """
  <div class="block">
    <p style="margin-bottom:0;">[PLACEHOLDER: go-live timeline once pivotal trial sales clearance allows public checkout]</p>
  </div>
"""

EPRO_OVERVIEW = """
  <div class="block">
    <div class="section-eyebrow">Challenge</div>
    <p>As WAVE moves toward FDA clearance, the ePRO app needs to make patient-reported outcomes effortless and trustworthy, since a $2M pivotal clinical trial's data integrity depends on honest, low-friction reporting from an estimated 250+ participants.</p>
    <div class="section-eyebrow" style="margin-top:20px;">Approach</div>
    <p>UX and design system development for the app where trial participants report outcomes directly, currently in progress.</p>
  </div>
  <div class="block">
    <div class="stats-band">
      <div class="stat"><b>$2M</b><span>Pivotal clinical trial</span></div>
      <div class="stat"><b>250+</b><span>Estimated participants</span></div>
      <div class="stat"><b>—</b><span>[Placeholder, current phase]</span></div>
    </div>
  </div>
"""

epro_block = extract_between(bak, '<span class="subproject-tag">ePRO Clinical Trial App</span>', '<div class="block">\n    <h3>Build status</h3>')
EPRO_DESIGN = f"""
  <div class="block">
    <div class="subproject">
      <span class="subproject-tag">ePRO Clinical Trial App</span>
{epro_block.strip()}
    </div>
  </div>
"""

EPRO_OUTCOME = """
  <div class="block">
    <div class="gallery-item wide">[PLACEHOLDER: trial protocol validation and participant usability outcomes]</div>
  </div>
"""

EPRO_PROGRESS = """
  <div class="block">
    <p style="margin-bottom:0;">[PLACEHOLDER: next ePRO build milestones aligned to trial start]</p>
  </div>
"""

def wrap_panel(project, panel, inner, active=False):
    cls = "tab-panel active" if active else "tab-panel"
    return f'<div class="{cls}" data-panel="{panel}">\n{inner}\n</div>'

def content_set(project, panels, active=False):
    cls = "tab-content-set active" if active else "tab-content-set"
    body = "\n".join(panels)
    return f'<div class="{cls}" data-project="{project}">\n{body}\n</div>'

set0 = content_set("0", [
    wrap_panel("0", "overview", br_overview, True),
    wrap_panel("0", "design", br_design),
    wrap_panel("0", "outcome", br_outcome),
    wrap_panel("0", "progress", br_progress),
], active=True)

set1 = content_set("1", [
    wrap_panel("1", "overview", ECO_OVERVIEW),
    wrap_panel("1", "design", ECO_DESIGN),
    wrap_panel("1", "outcome", ECO_OUTCOME),
    wrap_panel("1", "progress", ECO_PROGRESS),
])

set2 = content_set("2", [
    wrap_panel("2", "overview", EPRO_OVERVIEW),
    wrap_panel("2", "design", EPRO_DESIGN),
    wrap_panel("2", "outcome", EPRO_OUTCOME),
    wrap_panel("2", "progress", EPRO_PROGRESS),
])

nav = bak.split("<div class=\"tab-nav-anchor\"")[1].split("</div>\n</div>\n</div>")[0]
nav_block = """<div id="tabSection">
  <div class="tab-nav-anchor\"""" + nav + """</div>
</div>
</div>
</div>
"""

# Fix nav_block - need proper structure from backup
nav_html = """
<div id="tabSection">
<div class="tab-nav-anchor" id="tabNavAnchor">
  <div class="tab-nav-sentinel" id="tabNavSentinel" aria-hidden="true"></div>
  <div class="tab-nav-spacer" id="tabNavSpacer" aria-hidden="true"></div>
  <div class="tab-nav-wrap" id="tabNavWrap">
  <div class="tab-nav" id="tabNav">
  <div class="tab-track">
    <button type="button" class="tab-btn active" data-tab="overview">Overview</button>
    <button type="button" class="tab-btn" data-tab="design">Design &amp; Process</button>
    <button type="button" class="tab-btn" data-tab="outcome">Outcome</button>
    <button type="button" class="tab-btn" data-tab="progress">Upcoming</button>
  </div>
</div>
</div>
</div>
"""

header = """
<nav>
  <a href="../#work" class="back-link">
    <svg viewBox="0 0 100 100" fill="none"><path d="M75 50 H30 M50 25 L25 50 L50 75" stroke="currentColor" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></svg>
    All work
  </a>
  <a href="/" class="nav-mark" aria-label="Back to home">
    <svg width="105" height="23" viewBox="150 95 465 115" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="navLogoGradWV" x1="0" y1="73.98" x2="0" y2="314.82" gradientUnits="userSpaceOnUse">
          <stop offset=".04" stop-color="#254444"/><stop offset=".34" stop-color="#2a4748"/><stop offset=".69" stop-color="#385354"/><stop offset="1" stop-color="#4b6264"/>
        </linearGradient>
      </defs>
      <path fill="url(#navLogoGradWV)" d="M156.97,201.31l33.3-93.09,25.04-.25,36.15,93.34h-23.93l-7.85-18.87-33.12-.61-6.28,19.48h-23.32ZM213.42,163.28l-10.43-31.91-9.2,31.91h19.63Z"/>
      <polygon fill="url(#navLogoGradWV)" points="303 108.06 303 181.68 338.59 181.68 338.59 201.31 279.69 201.31 279.69 108.06 303 108.06"/>
      <polygon fill="url(#navLogoGradWV)" points="391.36 108.06 391.36 201.31 371.11 201.31 369.27 199.47 369.27 108.06 391.36 108.06"/>
      <path fill="url(#navLogoGradWV)" d="M510.31,113.06l-6.07,20.77c-24.52-14.96-57.03-9.44-54.03,25.21,1.63,18.8,18.53,26.29,35.7,23.33,7.25-1.25,12.91-5.63,19.55-8.04l6.09,18.3c-39.73,26.4-99.84.74-84.65-52.08,10.25-35.65,53.69-44.65,83.4-27.48Z"/>
      <path fill="url(#navLogoGradWV)" d="M608.56,108.06v18.4h-39.88c-2.97,3.94-3.01,14.32,0,18.4h37.43v18.4h-39.27v18.4h42.95v19.63h-65.04v-93.25h63.81Z"/>
    </svg>
  </a>
</nav>

<header class="cs-header">
  <div class="title-row">
    <h1>WAVE</h1>
    <span class="tag t1">Branding</span>
    <span class="tag">E-Commerce</span>
    <span class="tag t2">Clinical App</span>
  </div>
  <p class="cs-sub">FDA Medical Device · Women's Health · Brand, Product &amp; Commerce Systems</p>
  <p class="hub-lead">Three bodies of work on one medical device.</p>

  <div class="hub-cards" id="cardsRow">
    <button type="button" class="hub-card" data-project="0" aria-pressed="true">
      <div class="hub-card-thumb hub-card-thumb--brand"><span class="placeholder-note">[IMG: logo before / after]</span></div>
      <div class="hub-card-body">
        <div class="hub-card-head"><h3>Product Branding</h3><span class="hub-card-selected">Selected</span></div>
        <p class="hub-card-desc">Evolving a clinical medical device into a warm, human-centered wellness brand.</p>
      </div>
    </button>
    <button type="button" class="hub-card" data-project="1" aria-pressed="false">
      <div class="hub-card-thumb hub-card-thumb--commerce"><span class="placeholder-note">[IMG: storefront home page, desktop]</span></div>
      <div class="hub-card-body">
        <div class="hub-card-head"><h3>E-Commerce Site</h3><span class="hub-card-selected">Selected</span></div>
        <p class="hub-card-desc">A custom storefront and clinician site, built solo, ready to launch once trials allow a sale.</p>
      </div>
    </button>
    <button type="button" class="hub-card" data-project="2" aria-pressed="false">
      <div class="hub-card-thumb hub-card-thumb--epro"><span class="placeholder-note">[IMG: ePRO app screens]</span></div>
      <div class="hub-card-body">
        <div class="hub-card-head"><h3>ePRO App</h3><span class="hub-card-selected">Selected</span></div>
        <p class="hub-card-desc">Patient-reported outcomes for a $2M pivotal trial with 250+ participants.</p>
      </div>
    </button>
  </div>

  <p class="meta-note" style="max-width:none; margin-top:24px;">WAVE is an active client engagement for a company I co-founded. Serving as Creative Director, I established the brand and product vision while leading design execution alongside a second designer. We are currently building an ePRO (electronic patient-reported outcomes) app as our next product phase, alongside the company's website and e-commerce experience.</p>
  <div class="meta-row" style="border-top:none; padding-top:0; padding-bottom:10px; margin-top:20px;">
    <div class="meta-item"><span>Role</span><b>Creative Director, Brand &amp; Product</b></div>
    <div class="meta-item"><span>Scope</span><b>Brand System + Packaging + E-commerce site + Clinical App (ePRO)</b></div>
    <div class="meta-item"><span>Timeline</span><b>Ongoing</b></div>
    <div class="meta-item"><span>Year</span><b>2024-Present</b></div>
    <div class="meta-item"><span>Status</span><b>Live · Expanding</b></div>
    <div class="meta-item"><span>Team</span><b>With 3 Teammates</b></div>
  </div>
</header>
"""

footer_and_scripts = bak.split("<footer>")[1]

hub_js = """
<script>
(function(){
  const cards = Array.from(document.querySelectorAll('.hub-card'));
  const sets = Array.from(document.querySelectorAll('.tab-content-set'));
  const tabBtns = Array.from(document.querySelectorAll('.tab-btn'));
  const tabSection = document.getElementById('tabSection');
  let activeProject = '0';

  function activeSet(){
    return document.querySelector('.tab-content-set.active');
  }

  function setTab(tab){
    const set = activeSet();
    if(!set) return;
    tabBtns.forEach(b=> b.classList.toggle('active', b.dataset.tab === tab));
    set.querySelectorAll('.tab-panel').forEach(p=>{
      p.classList.toggle('active', p.dataset.panel === tab);
    });
    if(window.Relay && typeof Relay.activatePanel === 'function'){
      const panel = set.querySelector('.tab-panel.active');
      if(panel) Relay.activatePanel(panel);
    }
    wireContinueButtons();
  }

  function selectProject(project, opts){
    const scrollMobile = opts && opts.scrollMobile;
    const same = activeProject === project;
    activeProject = project;
    cards.forEach(c=>{
      const on = c.dataset.project === project;
      c.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
    sets.forEach(s=>{
      s.classList.toggle('active', s.dataset.project === project);
    });
    setTab('overview');
    if(scrollMobile && !same && window.matchMedia('(max-width: 760px)').matches){
      tabSection.scrollIntoView({behavior:'smooth', block:'start'});
    }
  }

  cards.forEach(card=>{
    card.addEventListener('click', e=>{
      e.stopPropagation();
      const p = card.dataset.project;
      selectProject(p, {scrollMobile: true});
    });
  });

  document.addEventListener('click', e=>{
    if(e.target.closest('#cardsRow') || e.target.closest('#tabSection')) return;
    if(activeProject !== '0') selectProject('0', {scrollMobile: false});
  });

  tabBtns.forEach(btn=>{
    btn.addEventListener('click', e=>{
      e.stopPropagation();
      setTab(btn.dataset.tab);
      const set = activeSet();
      const panel = set && set.querySelector('.tab-panel.active');
      if(panel){
        const panelTop = panel.getBoundingClientRect().top + window.scrollY;
        window.scrollTo({top: panelTop - 130, behavior:'smooth'});
      }
    });
  });

  function wireContinueButtons(){
    document.querySelectorAll('.panel-next').forEach(n=>n.remove());
    const set = activeSet();
    if(!set) return;
    const tabs = ['overview','design','outcome','progress'];
    tabs.forEach((tab, index)=>{
      const panel = set.querySelector('.tab-panel[data-panel="'+tab+'"]');
      if(!panel) return;
      if(index < tabs.length - 1){
        const nextTab = tabs[index + 1];
        const continueBtn = document.createElement('button');
        continueBtn.type = 'button';
        continueBtn.className = 'panel-next';
        continueBtn.innerHTML = `Continue
          <svg viewBox="0 0 100 100" fill="none"><path d="M25 50 H75 M55 25 L80 50 L55 75" stroke="currentColor" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
        continueBtn.addEventListener('click', ()=> setTab(nextTab));
        panel.appendChild(continueBtn);
      }
    });
    const nextProjectEl = document.querySelector('.next-project');
    const brandingOutcome = document.querySelector('.tab-content-set[data-project="0"] .tab-panel[data-panel="outcome"]');
    if(nextProjectEl && brandingOutcome && !brandingOutcome.contains(nextProjectEl)){
      nextProjectEl.remove();
      brandingOutcome.appendChild(nextProjectEl);
    }
  }

  selectProject('0', {scrollMobile: false});
})();
"""

# Fix wrap_panel - data-project attribute on panels for scoping? User said data-project on sets only, panels have data-panel only
def wrap_panel_fixed(project, panel, inner, active=False):
    cls = "tab-panel active" if active else "tab-panel"
    return f'<div class="{cls}" data-panel="{panel}">\n{inner}\n</div>'

set0 = content_set("0", [
    wrap_panel_fixed("0", "overview", br_overview, True),
    wrap_panel_fixed("0", "design", br_design),
    wrap_panel_fixed("0", "outcome", br_outcome),
    wrap_panel_fixed("0", "progress", br_progress),
], active=True)

set1 = content_set("1", [
    wrap_panel_fixed("1", "overview", ECO_OVERVIEW),
    wrap_panel_fixed("1", "design", ECO_DESIGN),
    wrap_panel_fixed("1", "outcome", ECO_OUTCOME),
    wrap_panel_fixed("1", "progress", ECO_PROGRESS),
])

set2 = content_set("2", [
    wrap_panel_fixed("2", "overview", EPRO_OVERVIEW),
    wrap_panel_fixed("2", "design", EPRO_DESIGN),
    wrap_panel_fixed("2", "outcome", EPRO_OUTCOME),
    wrap_panel_fixed("2", "progress", EPRO_PROGRESS),
])

body = header + nav_html + "\n" + set0 + "\n" + set1 + "\n" + set2 + "\n\n<footer>" + footer_and_scripts
body = body.split("<script>")[0] + hub_js + "\n" + "<script>" + body.split("<script>", 1)[1]

# Replace old tab script with hub only - remove duplicate tab handlers from footer scripts
parts = body.split("<script>")
# parts[0] html, then clarity, then old scripts - simplify: rebuild scripts section
html_before_scripts = body.split("<script>")[0]
clarity = extract_between(bak, "<script type=\"text/javascript\">", "</script>")
sticky = bak.split("backToTop.addEventListener")[0].split("(function(){")[-1]
# use scripts from bak from sticky tab onwards
scripts_tail = """
(function(){
  const tabWrap = document.getElementById('tabNavWrap');
  const sentinel = document.getElementById('tabNavSentinel');
  const spacer = document.getElementById('tabNavSpacer');
  if(!tabWrap || !sentinel || !spacer) return;
  const stickTop = 65;
  let isStuck = false;
  let cachedHeight = 0;
  function setSticky(stuck){
    if(stuck === isStuck) return;
    if(stuck){
      cachedHeight = tabWrap.offsetHeight;
      spacer.style.height = cachedHeight + 'px';
      tabWrap.classList.add('is-sticky');
      isStuck = true;
    } else {
      tabWrap.classList.remove('is-sticky');
      spacer.style.height = '0px';
      cachedHeight = 0;
      isStuck = false;
    }
  }
  function updateSticky(){
    setSticky(sentinel.getBoundingClientRect().top < stickTop);
  }
  const observer = new IntersectionObserver(()=>{ updateSticky(); }, { root:null, threshold:[0] });
  observer.observe(sentinel);
  window.addEventListener('scroll', updateSticky, {passive:true});
  window.addEventListener('resize', ()=>{
    if(isStuck){
      cachedHeight = tabWrap.offsetHeight;
      spacer.style.height = cachedHeight + 'px';
    }
    updateSticky();
  });
  updateSticky();
})();
const backToTop = document.getElementById('backToTop');
window.addEventListener('scroll', ()=>{
  if(window.scrollY > 500){ backToTop.classList.add('show'); }
  else{ backToTop.classList.remove('show'); }
});
backToTop.addEventListener('click', ()=>{ window.scrollTo({top:0, behavior:'smooth'}); });
"""

final = html_before_scripts + "<script type=\"text/javascript\">" + clarity.replace("<script type=\"text/javascript\">", "").replace("</script>", "") + "</script>\n" + hub_js + "\n<script>\n" + scripts_tail + "\n</script>\n\n<script src=\"/assets/js/relay.js\"></script>\n</body>\n</html>\n"

# clarity extract fix
clarity_script = re.search(r'<script type="text/javascript">\s*\(function\(c,l,a,r,i,t,y\).*?</script>', bak, re.S).group(0)

final = (
    head.replace("<style>", "<style>", 1).replace(bak.split("<style>")[1].split("</style>")[0], style)
    if False else None
)

# simpler: replace style in bak full doc
full = bak.split("</style>")[0] + HUB_CSS + "\n</style>" + bak.split("</style>", 1)[1]
# cut body from nav to footer and replace
pre = full.split("<nav>")[0]
post = full.split("<footer>")[1]
assembled = pre + header.lstrip() + nav_html + set0 + set1 + set2 + "\n\n<footer>" + post
# replace scripts between first hub script area
assembled = re.sub(
    r'<script>\s*document\.querySelectorAll\(\'\.tab-btn\'\).*?backToTop\.addEventListener\([^)]+\)[^;]+;\s*\)\s*;',
    hub_js + "\n<script>\n" + scripts_tail,
    assembled,
    count=1,
    flags=re.S
)

out_path.write_text(assembled)
print("Wrote", out_path, "bytes", out_path.stat().st_size)
