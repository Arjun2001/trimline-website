(function(){
  var h=document.querySelector('header.site'),tt=document.querySelector('.to-top');
  function onScroll(){var y=window.scrollY;h&&h.classList.toggle('scrolled',y>10);tt&&tt.classList.toggle('show',y>700)}
  window.addEventListener('scroll',onScroll,{passive:true});onScroll();
  tt&&tt.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'})});

  // mega menu (click for touch / keyboard)
  document.querySelectorAll('.has-mega>button').forEach(function(b){
    b.addEventListener('click',function(e){e.stopPropagation();var p=b.parentElement;var o=p.classList.toggle('open');b.setAttribute('aria-expanded',o)});
  });
  document.addEventListener('click',function(){document.querySelectorAll('.has-mega.open').forEach(function(p){p.classList.remove('open')})});

  // drawer
  var d=document.querySelector('.drawer');
  document.querySelectorAll('[data-drawer]').forEach(function(b){b.addEventListener('click',function(){d.classList.toggle('open');document.body.style.overflow=d.classList.contains('open')?'hidden':''})});
  d&&d.addEventListener('click',function(e){if(e.target===d){d.classList.remove('open');document.body.style.overflow=''}});

  // image fallbacks -> designed placeholder
  document.querySelectorAll('.prod img').forEach(function(img){
    function fail(){img.closest('.prod').classList.add('noimg')}
    if(img.complete&&img.naturalWidth===0)fail();else img.addEventListener('error',fail);
  });
  document.querySelectorAll('img[data-hide-on-error]').forEach(function(img){
    function fail(){var t=img.closest('[data-hide-wrap]')||img;t.style.display='none'}
    if(img.complete&&img.naturalWidth===0)fail();else img.addEventListener('error',fail);
  });

  document.querySelectorAll('.hv-card img,.showcase img').forEach(function(img){function f(){img.style.visibility='hidden'}if(img.complete&&img.naturalWidth===0)f();else img.addEventListener('error',f)});

  // reveal on scroll
  var els=document.querySelectorAll('.rv');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12,rootMargin:'0px 0px -40px 0px'});
    els.forEach(function(el){io.observe(el)});
  } else els.forEach(function(el){el.classList.add('in')});

  // count up
  document.querySelectorAll('[data-count]').forEach(function(el){
    var end=+el.dataset.count,suf=el.dataset.suffix||'',done=false;
    function run(){if(done)return;done=true;var t0=performance.now();(function step(t){var p=Math.min(1,(t-t0)/1400),v=Math.round(end*(1-Math.pow(1-p,3)));el.innerHTML=v+(suf?'<sup>'+suf+'</sup>':'');if(p<1)requestAnimationFrame(step)})(t0)}
    if('IntersectionObserver' in window){new IntersectionObserver(function(es,o){if(es[0].isIntersecting){run();o.disconnect()}}).observe(el)}else run();
  });

  // hero parallax
  var hv=document.querySelector('.hero-visual');
  if(hv&&matchMedia('(pointer:fine)').matches){
    document.querySelector('.hero').addEventListener('mousemove',function(e){
      var r=hv.getBoundingClientRect(),x=(e.clientX-r.left-r.width/2)/r.width,y=(e.clientY-r.top-r.height/2)/r.height;
      hv.querySelectorAll('.hv-card').forEach(function(c,i){var k=(i+1)*10;c.style.translate=(x*k)+'px '+(y*k)+'px'});
    });
  }

  // prefill enquiry form from ?product=
  var f=document.querySelector('form[name=enquiry]');
  if(f){
    var q=new URLSearchParams(location.search),p=q.get('product'),c=q.get('category');
    if(p){f.querySelector('[name=subject]').value='Quote request: '+p;var m=f.querySelector('[name=message]');m.value='Hello, I would like a quotation and more information on the '+p+'.';}
    if(c){var s=f.querySelector('[name=category]');[].forEach.call(s.options,function(o){if(o.value===c)s.value=c})}
    if(q.get('sent')){document.querySelector('.form-ok').classList.remove('hidden');f.classList.add('hidden')}
  }

  // product search
  var si=document.getElementById('psearch');
  if(si&&window.PRODUCTS){
    var out=document.getElementById('presults'),cats=document.getElementById('pcats');
    function render(){
      var v=si.value.trim().toLowerCase();
      if(!v){out.innerHTML='';cats.style.display='';return}
      cats.style.display='none';
      var r=PRODUCTS.filter(function(p){return (p.n+' '+p.c+' '+p.b+' '+p.k).toLowerCase().indexOf(v)>-1}).slice(0,30);
      out.innerHTML=r.length?r.map(function(p){return '<a class="res-item" href="'+p.u+'"><div class="ic">'+p.i+'</div><div><b>'+p.n+'</b><span>'+p.c+(p.b?' · '+p.b:'')+'</span></div></a>'}).join(''):'<p class="empty">No products match “'+si.value.replace(/</g,'&lt;')+'”. Try a brand like “ZOLL” or a word like “ventilator”.</p>';
    }
    si.addEventListener('input',render);
    document.addEventListener('keydown',function(e){if(e.key==='/'&&document.activeElement!==si){e.preventDefault();si.focus()}});
  }

  var y=document.getElementById('yr');y&&(y.textContent=new Date().getFullYear());
})();
(function(){
  // scroll progress + band parallax
  var pb=document.querySelector('.progress'),bands=document.querySelectorAll('.band .bg');
  function sc(){var h=document.documentElement,max=h.scrollHeight-h.clientHeight;pb&&(pb.style.width=(max>0?h.scrollTop/max*100:0)+'%');
    bands.forEach(function(b){var r=b.parentElement.getBoundingClientRect();if(r.bottom>0&&r.top<innerHeight){b.style.transform='translateY('+((r.top+r.height/2-innerHeight/2)*-.12)+'px)'}})}
  addEventListener('scroll',sc,{passive:true});sc();

  // ---------- quote list ----------
  var KEY='trimline-quote',mem=[];
  function load(){try{return JSON.parse(localStorage.getItem(KEY))||[]}catch(e){return mem}}
  function save(l){mem=l;try{localStorage.setItem(KEY,JSON.stringify(l))}catch(e){}}
  var list=load();
  var btn=document.querySelector('.qbtn'),panel=document.querySelector('.qpanel'),toast=document.querySelector('.toast');
  function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
  function has(n){return list.some(function(i){return i.n===n})}
  function sync(){
    if(btn){btn.querySelector('.c').textContent=list.length;btn.classList.toggle('show',list.length>0&&!document.querySelector('form[name=enquiry]'))}
    document.querySelectorAll('[data-add]').forEach(function(b){var on=has(b.dataset.add);b.classList.toggle('on',on);b.querySelector('span').textContent=on?'Added':'Add to quote'});
    if(panel){var box=panel.querySelector('.items');box.innerHTML=list.length?list.map(function(i,k){return '<div class="qitem"><div><b>'+esc(i.n)+'</b><span>'+esc(i.c)+'</span></div><button data-rm="'+k+'" aria-label="Remove">'+'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg></button></div>'}).join(''):'<p class="sub">Your list is empty.</p>'}
    var f=document.querySelector('form[name=enquiry]');
    if(f){var w=document.querySelector('.qlist-form'),hid=f.querySelector('[name=products]');
      hid.value=list.map(function(i){return i.n+' ('+i.c+')'}).join('; ');
      if(list.length){w.classList.remove('hidden');w.innerHTML='<b>Products in your quote ('+list.length+')</b><ul>'+list.map(function(i){return '<li>'+esc(i.n)+' — '+esc(i.c)+'</li>'}).join('')+'</ul>';
        var m=f.querySelector('[name=message]');if(!m.value&&!new URLSearchParams(location.search).get('product'))m.value='Hello, please send a quotation for the products listed above.'}
      else w.classList.add('hidden')}
  }
  function showToast(t){if(!toast)return;toast.querySelector('span').textContent=t;toast.classList.add('show');clearTimeout(showToast.t);showToast.t=setTimeout(function(){toast.classList.remove('show')},2200)}
  document.addEventListener('click',function(e){
    var a=e.target.closest('[data-add]');
    if(a){e.preventDefault();var n=a.dataset.add;if(has(n)){list=list.filter(function(i){return i.n!==n});showToast('Removed from your quote')}else{list.push({n:n,c:a.dataset.cat});showToast(n+' added to your quote');btn&&(btn.classList.remove('bump'),void btn.offsetWidth,btn.classList.add('bump'))}save(list);sync();return}
    var r=e.target.closest('[data-rm]');if(r){list.splice(+r.dataset.rm,1);save(list);sync();return}
    if(e.target.closest('.qbtn')){panel.classList.add('open');return}
    if(e.target===panel||e.target.closest('[data-qclose]')){panel.classList.remove('open')}
  });
  var f=document.querySelector('form[name=enquiry]');
  f&&f.addEventListener('submit',function(){save([])});
  sync();
})();
