(function(global){
  var MIN_VISIBLE = 500;
  var PAGE_READY_TIMEOUT = 2000;

  var FRAMES = [
    {vb:"6.46 118.62 80 80", fill:"#F2665A", d:['M70.48,162.44c3.32,3.45,2.87,4.1-.46,7.5-12.28,12.51-34.23,12.45-46.75.4-4.8-4.62-3.74-5.63.92-9.67,13.02-11.27,34.23-10.76,46.29,1.78ZM44.77,159.63c-7.44,1.38-5.77,13.29,1.66,13.06,8.92-.28,8.52-14.95-1.66-13.06ZM34.78,170.55c-.59-1.39-.93-2.84-.95-4.36-.03-2.01.73-3.44.73-5.29-.94,1.07-7.01,3.88-6.67,5.27l6.9,4.38ZM58.23,170.55l6.89-4.83-6.89-4.37c.58,3.02.79,6.21,0,9.19Z','M37.43,149.76c-3.38,3.35-10.47-3.99-6.83-7.06,3.51-2.96,9.58,4.33,6.83,7.06Z','M55.13,149.75c-2.71-2.86,4.42-10.28,7.45-6.77s-4.43,9.96-7.45,6.77Z','M45.69,137.99c4.83-1,6.09,8.47,1.23,9.1s-5.07-8.31-1.23-9.1Z']},
    {vb:"67.67 125.72 80 80", fill:"#F5A94A", d:['M95.55,143.47c1.14-.33,5.4-.61,5.43,1.1l.02,41.36-.7,1.71c-2.22.71-5.68,1.34-6.08-1.71-1.58-12.23,1.25-27.83,0-40.42,0-.91.4-1.78,1.32-2.04Z','M113.8,143.47c1.14-.33,5.4-.61,5.43,1.1l.02,41.36-.7,1.71c-2.22.71-5.68,1.34-6.08-1.71-1.58-12.23,1.25-27.83,0-40.42,0-.91.4-1.78,1.32-2.04Z','M129.96,154.31c.33,1.14.61,5.4-1.1,5.43l-41.36.02-1.71-.7c-.71-2.22-1.34-5.68,1.71-6.08,12.23-1.58,27.83,1.25,40.42,0,.91,0,1.78.4,2.04,1.32Z','M129.96,173.76c.33,1.14.61,5.4-1.1,5.43l-41.36.02-1.71-.7c-.71-2.22-1.34-5.68,1.71-6.08,12.23-1.58,27.83,1.25,40.42,0,.91,0,1.78.4,2.04,1.32Z']},
    {vb:"68.22 21.74 80 80", fill:"#F5A94A", d:['M107.97,55.23c2.37-3.08,3.99-6.6,6.48-9.62,5-6.07,14.77-13.15,23.07-11.97,1.83.26,2,.84,2.19,2.59,1.08,10.12-4.34,22.81-13.46,27.67l.3.99c2.96,1.38,4.22,5.32,4.49,8.38.24,2.64.38,13.87-.74,15.59-2.22,3.43-10.46-.97-13.07-2.75-4.26-2.9-6.56-6.23-9.03-10.69-2.07,4.86-5.13,8.73-9.71,11.45-3.23,1.91-11.93,6.14-12.66-.13-.45-3.84-.42-15.75,1.35-18.87.89-1.56,2.56-2.45,3.47-3.98-8.74-4.39-15.08-17.61-13.96-27.19.5-4.26,4.12-3.57,7.34-2.98,11.06,2.02,19.98,11.37,23.95,21.51ZM103.63,61.48c-3.16-9.54-10.17-19.44-20.68-21.15,1.41,10.85,9.16,20.86,20.68,21.15ZM133.45,40.33c-9.96,2.73-17.7,11.92-20.68,21.64,11.68-1.14,19.65-10.19,20.68-21.64ZM104.11,68.7h-7.94c-1.26,0-4.09,2.34-4.09,3.61v10.34c6.45-1.78,10.24-7.89,12.03-13.95ZM124.31,82.65v-11.3c0-.45-2.93-2.65-3.61-2.65h-7.94c1.21,6.05,5.77,11.76,11.54,13.95Z']},
    {vb:"131.78 113.82 80 80", fill:"#F2665A", d:['M155.87,155.24v14.98h31.96v-31.46h-23.22c-.14,0-1.17-.51-1.27-.84v-5.82c.12-.53,1.31-.72,1.8-.78,8.31-1.02,18.39.62,26.89-.02,1.8.28,2.34,1.11,2.66,2.83-.63,12.47,1.26,26.56.14,38.84-.12,1.34-.28,2.72-1.22,3.77h-44.04c-.77-.61-.65-1.42-.73-2.26-.49-5.24-.66-18.99,0-24.02.22-1.63.59-2.03,2.25-2.25,1.99-.26,14.95-.3,16.4.12,2.36.69,1.49,6.89.1,6.89h-11.73Z']},
    {vb:"11.06 70.93 80 80", fill:"#F5A94A", d:['M69.44,126.94c1.25-1.1-6.63-6.17-7.64-6.59-4.43-1.84-7.07-.77-11.06-1.42s-2.4-3.55-2.78-6.21c-1.13-7.98-8.53-15.4-16.35-17.1-5.16-1.12-10.6,1.29-8.15-6.78,1.33-2.11,10.41.03,12.66.78,9.78,3.25,17.29,12.12,18.88,22.31,10.08.04,20.23,7.08,23.51,16.68.64,1.86,1.38,3.31-.3,4.87l-53.45.45-1.51-.98c-.6-1.41-.5-5.99,1.5-5.99h44.69Z']},
    {vb:"131.83 19.09 80 80", fill:"#F5A94A", d:['M180.07,36.54c9.71-1.08,16.44,8.72,15.28,17.59-1.17,8.89-12.68,21.16-20.07,25.81-1.82,1.14-2.4,2.06-4.84,1.69-4.93-.74-17.04-14.46-19.43-19.12-4.35-8.47-4.77-21.84,6.23-24.97,6.18-1.76,10.12-.1,14.68,3.95,2.17-2.26,4.89-4.59,8.16-4.95ZM160.22,44.48c-1.79.4-4.05,2.91-4.34,4.73-1.32,8.15,6.3,16.91,12.16,21.76,4.07,3.37,4.36,1.92,8.21-1.39,5.12-4.4,16.79-17.46,9.03-23.77-7.2-5.86-9.03,6.8-13.81,6.49-4.23-.28-4.89-9.22-11.24-7.81Z']},
    {vb:"125.73 69.33 80 80", fill:"#F2665A", d:['M178.06,101.63l-26.46,26.2c-2.89,2.26-7.45-1.28-5.52-4.51l26.49-26.18h-13.23c-1.49-1.76-.72-4.9-.25-6.99h24.72c.77,0,1.66,2.4,1.76,3.23.4,3.4.52,18.39-.12,21.37-.73,3.35-7.38,1.84-7.38.61v-13.73Z']},
    {vb:"3.36 18.24 80 80", fill:"#F5A94A", d:['M54.52,35.36c4.85-.24,3.71,2.32,3.35,6.36-1.76,1.67-4.31.72-6.46,1.03-8.27,1.21-16.56,9.18-18.91,17.04-.82,2.73-.13,6.51-3.08,6.9-6,.79-4.65-5.05-3.62-9.12,3.19-12.59,16.03-21.58,28.72-22.22Z','M21.79,74.78c.45-.39,2.38-.58,3.1-.64,12.06-.93,25.29.74,37.48,0,3.81-.42,4.37,6.47,1.49,7l-41.99-.45c-1.13-.91-.92-5.19-.08-5.92Z']},
    {vb:"68.97 76.13 80 80", fill:"#F2665A", d:['M125.22,98.4l7.25,18.63-17.23,6.7-7.25-18.63,17.23-6.7M125.22,92.4c-.72,0-1.46.13-2.17.41l-17.23,6.7c-1.48.58-2.68,1.72-3.32,3.18-.64,1.46-.68,3.11-.1,4.59l7.25,18.63c.92,2.37,3.19,3.83,5.59,3.83.72,0,1.46-.13,2.17-.41l17.23-6.7c1.48-.58,2.68-1.72,3.32-3.18.64-1.46.68-3.11.1-4.59l-7.25-18.63c-.92-2.37-3.19-3.83-5.59-3.83h0Z','M102.94,107.42c.82,2.12,1.64,4.22,2.05,5.13.38.87,1.25,2.81,2.91,4.2-.03.1-.05.21-.08.31-.26,1.16-.17,2.37.27,3.48l2.12,5.44-15.81,6.15-7.22-18.57,15.77-6.14M106.4,99.63l-26.99,10.5,11.57,29.75,26.99-10.5-4.29-11.03s.33-1.46,2.29-1.46c.64,0,1.45.15,2.49.56.47.18.91.27,1.34.27,3.41,0,5.3-5.48,3.07-8.6-1.25-1.74-3.12-2.7-4.87-2.7s-3.43,1-4.15,3.22c-.63,1.94-1.2,2.63-1.71,2.63-.65,0-1.2-1.1-1.67-2.17-.85-1.91-4.07-10.47-4.07-10.47h0Z']}
  ];

  function injectStyles(){
    if (document.getElementById('relay-styles')) return;
    var style = document.createElement('style');
    style.id = 'relay-styles';
    style.textContent = '.relay-loader{position:fixed;inset:0;z-index:9999;background:var(--paper);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px;transition:opacity .5s ease,visibility .5s ease;}.relay-loader.is-hidden{opacity:0;visibility:hidden;pointer-events:none;}.relay-badge{border-radius:50%;background:var(--paper-alt);display:flex;align-items:center;justify-content:center;position:relative;transition:background .4s ease,transform .4s ease;}.relay-stage{position:relative;}.relay-stage svg{position:absolute;top:0;left:0;opacity:0;transform:scale(.85);transform-origin:center;transition:opacity .35s ease,transform .35s ease;}.relay-stage svg.is-active{opacity:1;transform:scale(1);}.relay-label{font-family:"Poppins",sans-serif;font-weight:600;font-size:12.5px;letter-spacing:.04em;color:var(--ink-soft);text-transform:uppercase;display:flex;text-align:center;}.relay-dots span{animation:relay-blink 1.4s infinite;opacity:0;}.relay-dots span:nth-child(2){animation-delay:.2s;}.relay-dots span:nth-child(3){animation-delay:.4s;}@keyframes relay-blink{0%,80%,100%{opacity:0;}40%{opacity:1;}}.relay-image-wrap{position:relative;overflow:hidden;border-radius:16px;background:var(--paper-alt);min-height:160px;}.relay-image-wrap img{position:relative;z-index:1;opacity:0;transition:opacity .4s ease;}.relay-image-wrap img.is-loaded{opacity:1;}.relay-image-placeholder{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;z-index:2;transition:opacity .5s ease;padding:16px;}.relay-image-placeholder.is-hidden{opacity:0;pointer-events:none;}';
    document.head.appendChild(style);
  }

  function buildStage(stage, iconSize){
    var svgns = 'http://www.w3.org/2000/svg';
    FRAMES.forEach(function(f){
      var svg = document.createElementNS(svgns,'svg');
      svg.setAttribute('viewBox', f.vb);
      svg.setAttribute('width', iconSize);
      svg.setAttribute('height', iconSize);
      svg.dataset.fill = f.fill;
      f.d.forEach(function(dstr){
        var path = document.createElementNS(svgns,'path');
        path.setAttribute('d', dstr);
        path.setAttribute('fill', f.fill);
        svg.appendChild(path);
      });
      stage.appendChild(svg);
    });
    stage.style.width = iconSize+'px';
    stage.style.height = iconSize+'px';
    return stage.querySelectorAll('svg');
  }

  function buildDots(container){
    var dots = document.createElement('span');
    dots.className = 'relay-dots';
    dots.style.display = 'inline-flex';
    ['.','.','.'].forEach(function(ch,i){
      var s = document.createElement('span');
      s.textContent = ch;
      s.style.animationDelay = (i*0.2)+'s';
      dots.appendChild(s);
    });
    container.appendChild(dots);
    return dots;
  }

  function contrastOf(fill){ return fill === '#F2665A' ? '#F5A94A' : '#F2665A'; }

  function runCycle(svgs){
    var i = 0;
    svgs[0].classList.add('is-active');
    var timer = setInterval(function(){
      svgs[i].classList.remove('is-active');
      i = (i + 1) % svgs.length;
      svgs[i].classList.add('is-active');
    }, 550);
    return {
      stop: function(){ clearInterval(timer); },
      current: function(){ return svgs[i]; }
    };
  }

  function whenPageReady(cb){
    var done = false;
    function run(){
      if(done) return;
      done = true;
      cb();
    }
    function onDomReady(){
      if(document.fonts && document.fonts.ready){
        document.fonts.ready.then(run).catch(run);
      } else {
        run();
      }
    }
    if(document.readyState === 'loading'){
      document.addEventListener('DOMContentLoaded', onDomReady, { once:true });
    } else {
      onDomReady();
    }
    setTimeout(run, PAGE_READY_TIMEOUT);
  }

  function deferMediaEl(el){
    if(el.dataset.lazySrc || !el.getAttribute('src')) return;
    el.dataset.lazySrc = el.getAttribute('src');
    el.removeAttribute('src');
    if(el.tagName === 'VIDEO') el.load();
  }

  function loadMediaEl(el, opts){
    opts = opts || {};
    if(!el.dataset.lazySrc || el.getAttribute('src')) return;
    el.setAttribute('src', el.dataset.lazySrc);
    if(el.tagName === 'VIDEO'){
      el.preload = opts.preload || 'metadata';
      if(el.hasAttribute('autoplay')){
        el.play().catch(function(){});
      }
    }
  }

  function deferPanelMedia(panel){
    panel.querySelectorAll('img[src], video[src]').forEach(deferMediaEl);
  }

  function markLazyImages(root){
    var scope = root || document;
    scope.querySelectorAll('img[data-relay]').forEach(function(img){
      if(img.closest('.hero-image') || img.closest('.cs-header > .header-top')) return;
      img.loading = 'lazy';
    });
  }

  function activatePanel(panel){
    if(!panel || panel.dataset.lazyLoaded === '1') return;
    panel.dataset.lazyLoaded = '1';
    panel.querySelectorAll('[data-lazy-src]').forEach(function(el){
      loadMediaEl(el, { preload: 'metadata' });
    });
    markLazyImages(panel);
    initImagesIn(panel);
  }

  function deferInactiveTabMedia(){
    document.querySelectorAll('.tab-panel:not(.active)').forEach(deferPanelMedia);
  }

  function initTabHooks(){
    document.addEventListener('click', function(e){
      var btn = e.target.closest('.tab-btn');
      if(!btn || !btn.dataset.tab) return;
      setTimeout(function(){
        var panel = document.querySelector('.tab-panel[data-panel="' + btn.dataset.tab + '"]');
        activatePanel(panel);
      }, 0);
    });
  }

  function tuneHeaderVideos(){
    document.querySelectorAll('.cs-header video[src]').forEach(function(video){
      if(!video.hasAttribute('preload')){
        video.preload = 'auto';
      }
    });
    document.querySelectorAll('.tab-panel video[src]').forEach(function(video){
      if(!video.closest('.hero-image')){
        video.preload = 'metadata';
      }
    });
  }

  function pageLoader(){
    injectStyles();
    var root = document.getElementById('relay-loader');
    if (!root) return;
    var badge = document.getElementById('relay-badge');
    var stage = document.getElementById('relay-stage');
    var labelText = document.getElementById('relay-label-text');
    var dotsEl = document.getElementById('relay-dots');
    badge.style.width = '96px';
    badge.style.height = '96px';
    var svgs = buildStage(stage, 52);
    var ctrl = runCycle(svgs);
    var shownAt = Date.now();

    function finish(){
      var elapsed = Date.now() - shownAt;
      var wait = elapsed < MIN_VISIBLE ? (MIN_VISIBLE - elapsed) : 0;
      setTimeout(function(){
        ctrl.stop();
        var finalFill = ctrl.current().dataset.fill;
        badge.style.background = contrastOf(finalFill);
        badge.style.transform = 'scale(1.08)';
        setTimeout(function(){ badge.style.transform = 'scale(1)'; }, 400);
        dotsEl.style.display = 'none';
        labelText.textContent = 'Ready';
        setTimeout(function(){ root.classList.add('is-hidden'); }, 900);
      }, wait);
    }

    whenPageReady(finish);
  }

  function imageLoader(img, opts){
    opts = opts || {};
    injectStyles();
    if (img.dataset.relayInit === '1') return;
    img.dataset.relayInit = '1';
    if (img.complete && img.naturalWidth !== 0){
      img.classList.add('is-loaded');
      return;
    }

    var delay = opts.delay != null ? opts.delay : 200;
    var slowAfter = opts.slowAfter != null ? opts.slowAfter : 4000;
    var aspect = opts.aspect || img.dataset.relayAspect || null;

    var wrap = document.createElement('div');
    wrap.className = 'relay-image-wrap';
    if (aspect) { wrap.style.aspectRatio = aspect; }
    img.parentNode.insertBefore(wrap, img);
    wrap.appendChild(img);

    var placeholder = document.createElement('div');
    placeholder.className = 'relay-image-placeholder';
    wrap.insertBefore(placeholder, img);

    var badge = document.createElement('div');
    badge.className = 'relay-badge';
    badge.style.width = '72px';
    badge.style.height = '72px';
    var stage = document.createElement('div');
    stage.className = 'relay-stage';
    badge.appendChild(stage);
    placeholder.appendChild(badge);

    var label = document.createElement('div');
    label.className = 'relay-label';
    var labelText = document.createElement('span');
    labelText.textContent = 'Loading';
    label.appendChild(labelText);
    var dotsEl = buildDots(label);
    placeholder.appendChild(label);

    var ctrl, showTimer, slowTimer, shownAt = null;

    showTimer = setTimeout(function(){
      var svgs = buildStage(stage, 40);
      ctrl = runCycle(svgs);
      shownAt = Date.now();
    }, delay);

    slowTimer = setTimeout(function(){
      if (shownAt) labelText.textContent = 'Still loading, hang tight';
    }, slowAfter);

    function settle(state){
      clearTimeout(showTimer);
      clearTimeout(slowTimer);
      var elapsed = shownAt ? Date.now() - shownAt : 0;
      var wait = shownAt && elapsed < MIN_VISIBLE ? (MIN_VISIBLE - elapsed) : 0;
      setTimeout(function(){
        if (ctrl) ctrl.stop();
        if (state === 'loaded'){
          img.classList.add('is-loaded');
          wrap.style.minHeight = '0';
          placeholder.classList.add('is-hidden');
          setTimeout(function(){ placeholder.remove(); }, 500);
        } else {
          labelText.textContent = 'Image unavailable';
          dotsEl.style.display = 'none';
        }
      }, wait);
    }

    img.addEventListener('load', function(){ settle('loaded'); }, { once:true });
    img.addEventListener('error', function(){ settle('error'); }, { once:true });
  }

  function initImagesIn(root){
    if(!root) return;
    root.querySelectorAll('img[data-relay]').forEach(function(img){
      imageLoader(img);
    });
  }

  function initImages(selector){
    document.querySelectorAll(selector || 'img[data-relay]').forEach(function(img){
      imageLoader(img);
    });
  }

  function boot(){
    Relay.pageLoader();
    if(document.querySelector('.tab-panel')){
      Relay.deferInactiveTabMedia();
      Relay.initTabHooks();
      Relay.tuneHeaderVideos();
      Relay.markLazyImages(document.querySelector('.cs-header'));
      Relay.markLazyImages(document.querySelector('.tab-panel.active'));
      Relay.initImagesIn(document.querySelector('.cs-header'));
      Relay.initImagesIn(document.querySelector('.tab-panel.active'));
      return;
    }
    Relay.initImages();
  }

  global.Relay = {
    pageLoader: pageLoader,
    imageLoader: imageLoader,
    initImages: initImages,
    initImagesIn: initImagesIn,
    deferInactiveTabMedia: deferInactiveTabMedia,
    activatePanel: activatePanel,
    markLazyImages: markLazyImages,
    initTabHooks: initTabHooks,
    tuneHeaderVideos: tuneHeaderVideos
  };

  if(document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})(window);
