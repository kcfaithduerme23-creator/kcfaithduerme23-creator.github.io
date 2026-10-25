

HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>KC Faith B. Duerme | BSIT Portfolio</title>
<meta name="description" content="Portfolio of KC Faith B. Duerme, BSIT student at Torres Capitol College. Campus Lost & Found System, Employee Information System, web development and database design.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Fraunces:opsz,wght@9..144,500;9..144,700&display=swap" rel="stylesheet">
<style>
:root{
  --ink:#17203a;        /* navy from the blazer */
  --paper:#fdf4f6;      /* blush paper */
  --rose:#b8345e;       /* thread accent */
  --rose-soft:#f6d5df;
  --slate:#586079;
  --line:rgba(23,32,58,.16);
  --white:#fff;
  --serif:"Fraunces",Georgia,"Times New Roman",serif;
  --sans:"DM Sans",system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
  color-scheme:light;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:84px}
body{margin:0;background:var(--paper);color:var(--ink);font:400 17px/1.65 var(--sans);-webkit-font-smoothing:antialiased;
  padding-bottom:env(safe-area-inset-bottom,0px)}
a{color:inherit}
:focus-visible{outline:3px solid var(--rose);outline-offset:3px;border-radius:4px}
h1,h2,h3{font-family:var(--serif);font-weight:700;line-height:1.1;margin:0;letter-spacing:-.01em}
p{margin:0 0 1em}
.wrap{max-width:1080px;margin:0 auto;padding:0 24px}

/* ---------- header ---------- */
header.top{position:sticky;top:0;z-index:10;background:rgba(253,244,246,.92);backdrop-filter:blur(10px);
  border-bottom:1px solid var(--line);padding-top:env(safe-area-inset-top,0px)}
header.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;min-height:64px}
.mark{font-family:var(--serif);font-weight:700;font-size:1.1rem;text-decoration:none;white-space:nowrap}
.mark span{color:var(--rose)}
nav ul{display:flex;gap:4px;list-style:none;margin:0;padding:0}
nav a{display:block;padding:8px 12px;border-radius:8px;text-decoration:none;font-size:.95rem;font-weight:500;color:var(--slate)}
nav a:hover{color:var(--ink);background:var(--rose-soft)}
nav a[aria-current=true]{color:var(--ink);box-shadow:inset 0 -2px 0 var(--rose);border-radius:0}

/* ---------- hero ---------- */
.hero{padding:72px 0 88px}
.hero .wrap{display:grid;gap:56px;align-items:center}
@media(min-width:900px){.hero .wrap{grid-template-columns:1.1fr .9fr}}
.hero h1{font-size:clamp(2.5rem,6.2vw,4.4rem)}
.hero .lede{font-size:1.15rem;color:var(--slate);max-width:46ch;margin:22px 0 30px}
.btns{display:flex;flex-wrap:wrap;gap:12px}
.btn{display:inline-block;padding:13px 24px;border-radius:999px;font:700 .98rem var(--sans);text-decoration:none;border:2px solid var(--ink);color:var(--ink);background:transparent;cursor:pointer}
.btn:hover{background:var(--ink);color:var(--white)}
.btn.fill{background:var(--rose);border-color:var(--rose);color:var(--white)}
.btn.fill:hover{background:var(--ink);border-color:var(--ink)}

/* the claim ticket: the one memorable element */
.ticket-wrap{display:flex;justify-content:center}
.ticket{width:min(360px,100%);filter:drop-shadow(0 18px 24px rgba(23,32,58,.18));transform:rotate(-2.5deg);
  animation:print 1s cubic-bezier(.2,.8,.2,1) both}
@keyframes print{from{transform:translateY(-46px) rotate(-6deg);opacity:0}to{transform:rotate(-2.5deg);opacity:1}}
.ticket .head{background:var(--ink);color:var(--white);border-radius:16px 16px 0 0;padding:14px 20px;display:flex;justify-content:space-between;align-items:baseline;gap:12px}
.ticket .head b{font-family:var(--serif);font-size:1.15rem}
.ticket .head small{opacity:.75;font-size:.8rem}
.ticket .body{background:var(--white);padding:20px;display:grid;grid-template-columns:116px 1fr;gap:16px}
.ticket img{width:116px;height:150px;object-fit:cover;object-position:top;border-radius:8px;display:block;background:var(--rose-soft)}
.ticket dl{margin:0;display:grid;gap:10px;align-content:start}
.ticket dt{font-size:.78rem;color:var(--slate);line-height:1.2}
.ticket dd{margin:0;font-weight:700;font-size:.95rem;line-height:1.25}
.ticket .stub{position:relative;background:var(--white);border-top:2px dashed var(--line);border-radius:0 0 16px 16px;padding:16px 20px 18px}
.ticket .stub::before,.ticket .stub::after{content:"";position:absolute;top:-12px;width:22px;height:22px;border-radius:50%;background:var(--paper)}
.ticket .stub::before{left:-11px}.ticket .stub::after{right:-11px}
.bars{height:34px;background:repeating-linear-gradient(90deg,var(--ink) 0 2px,transparent 2px 5px,var(--ink) 5px 6px,transparent 6px 10px,var(--ink) 10px 13px,transparent 13px 15px);opacity:.85;border-radius:2px}
.ticket .stub p{margin:10px 0 0;font-size:.82rem;color:var(--slate)}

/* ---------- sections ---------- */
section{padding:88px 0;border-top:1px solid var(--line)}
.sec-head{display:grid;gap:10px;margin-bottom:44px;max-width:60ch}
.sec-head h2{font-size:clamp(1.9rem,4vw,2.7rem)}
.sec-head p{color:var(--slate);margin:0}

/* about */
.about{display:grid;gap:48px}
@media(min-width:900px){.about{grid-template-columns:1.2fr .8fr}}
.about p{max-width:62ch}
.timeline{list-style:none;margin:0;padding:0 0 0 22px;border-left:2px solid var(--rose-soft)}
.timeline li{position:relative;padding:0 0 26px}
.timeline li::before{content:"";position:absolute;left:-30px;top:6px;width:14px;height:14px;border-radius:50%;background:var(--paper);border:3px solid var(--rose)}
.timeline b{display:block;font-family:var(--serif);font-size:1.05rem}
.timeline span{color:var(--slate);font-size:.95rem}

/* projects */
.project{display:grid;gap:36px;align-items:center;padding:12px 0 64px}
.project+.project{padding-top:64px;border-top:1px solid var(--line)}
.project:last-child{padding-bottom:12px}
@media(min-width:900px){.project{grid-template-columns:1fr 1fr;gap:64px}.project.flip .visual{order:-1}}
.project h3{font-size:clamp(1.5rem,3vw,2.1rem);margin-bottom:6px}
.project .role{color:var(--rose);font-weight:700;margin-bottom:16px}
.project ul{padding-left:20px;margin:0 0 16px}
.project li{margin-bottom:4px}
.facts{margin:0;display:grid;gap:6px;font-size:.95rem}
.facts div{display:grid;grid-template-columns:96px 1fr;gap:12px}
.facts dt{font-weight:700}.facts dd{margin:0;color:var(--slate)}

/* mock screen */
.screen{background:var(--white);border:1px solid var(--line);border-radius:14px;overflow:hidden;box-shadow:0 20px 40px -24px rgba(23,32,58,.35)}
.screen .bar{display:flex;align-items:center;gap:7px;padding:11px 14px;background:var(--ink);color:var(--white);font-size:.85rem}
.screen .bar i{width:10px;height:10px;border-radius:50%;background:var(--rose-soft);opacity:.8}
.screen .bar span{margin-left:8px}
.screen .find{margin:16px;padding:10px 14px;border:1px solid var(--line);border-radius:8px;color:var(--slate);font-size:.9rem}
.screen .row{display:grid;grid-template-columns:1fr auto;gap:12px;align-items:center;padding:13px 16px;border-top:1px solid var(--line)}
.screen .row b{display:block;font-size:.95rem}
.screen .row small{color:var(--slate)}
.pill{font-size:.78rem;font-weight:700;padding:4px 11px;border-radius:999px;background:var(--rose-soft);color:#7d1f40;white-space:nowrap}
.pill.ok{background:#d9ecdf;color:#1d5a35}
.pill.wait{background:#fbe8c4;color:#7a4e07}
.pill.mute{background:#e4e5e9;color:#34363e}
.caption{font-size:.82rem;color:var(--slate);margin:10px 4px 0}

/* EIS screen: graphite, like the app itself */
.screen.eis .bar{background:#25262c}
.screen.eis .bar i{background:#c9ced6}

/* neon wheel */
.neon{background:#120c24;border-radius:14px;padding:36px 20px;display:grid;justify-items:center;gap:18px;box-shadow:0 20px 40px -24px rgba(18,12,36,.7)}
.wheel{width:min(230px,70%);aspect-ratio:1;border-radius:50%;cursor:pointer;border:6px solid #120c24;outline:3px solid #ff4fa3;position:relative;
  background:conic-gradient(#ff4fa3 0 60deg,#7a5cff 60deg 120deg,#2ee6d6 120deg 180deg,#ffd447 180deg 240deg,#ff7a45 240deg 300deg,#8dff6a 300deg 360deg);
  box-shadow:0 0 36px rgba(255,79,163,.55);transition:transform 2.4s cubic-bezier(.12,.7,.1,1)}
.wheel::after{content:"";position:absolute;inset:38%;border-radius:50%;background:#120c24;border:3px solid #ff4fa3}
.neon p{margin:0;color:#e8dcff;font-size:.9rem;text-align:center}

/* skills */
.skills{display:grid;gap:0;border-top:1px solid var(--line)}
.skills div{display:grid;gap:4px;padding:20px 0;border-bottom:1px solid var(--line)}
@media(min-width:760px){.skills div{grid-template-columns:200px 1fr;gap:32px}}
.skills dt{font-family:var(--serif);font-weight:700;font-size:1.1rem}
.skills dd{margin:0;color:var(--slate)}

/* recognition */
.recog{display:grid;gap:40px;align-items:start}
@media(min-width:900px){.recog{grid-template-columns:.8fr 1.2fr}}
.recog h3{font-size:1.25rem;margin-bottom:6px}
.recog .item{padding:0 0 24px}
.recog .item p{color:var(--slate);margin:0}
.cert{display:block;width:100%;height:auto;border:1px solid var(--line);border-radius:10px;background:var(--white)}

/* contact */
.contact{display:grid;gap:48px}
@media(min-width:900px){.contact{grid-template-columns:.9fr 1.1fr}}
.contact dl{margin:0;display:grid;gap:16px}
.contact dt{font-size:.85rem;color:var(--slate)}
.contact dd{margin:0;font-weight:500;overflow-wrap:anywhere}
form{display:grid;gap:14px}
label{display:grid;gap:6px;font-weight:500;font-size:.95rem}
input,textarea{width:100%;font:inherit;color:var(--ink);background:var(--white);border:1.5px solid var(--line);border-radius:10px;padding:12px 14px}
input:focus,textarea:focus{outline:3px solid var(--rose-soft);border-color:var(--rose)}
textarea{min-height:140px;resize:vertical}
form .btn{justify-self:start}

footer{border-top:1px solid var(--line);padding:28px 0 36px;color:var(--slate);font-size:.9rem}
footer .wrap{display:flex;flex-wrap:wrap;justify-content:space-between;gap:8px}

@media(max-width:620px){
  body{font-size:16px}
  header.top .wrap{flex-direction:column;align-items:flex-start;gap:0;padding-top:8px}
  nav ul{flex-wrap:wrap}
  .hero{padding:44px 0 64px}
  section{padding:64px 0}
  .ticket .body{grid-template-columns:96px 1fr}
  .ticket img{width:96px;height:128px}
}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}.ticket{animation:none}.wheel{transition:none}}
</style>
</head>
<body>

<header class="top">
  <div class="wrap">
    <a class="mark" href="#home">KC Faith <span>B.</span> Duerme</a>
    <nav aria-label="Main">
      <ul>
        <li><a href="#about">About</a></li>
        <li><a href="#projects">Projects</a></li>
        <li><a href="#skills">Skills</a></li>
        <li><a href="#recognition">Recognition</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </nav>
  </div>
</header>

<main id="home">

<div class="hero">
  <div class="wrap">
    <div>
      <h1>I build campus systems people can actually use.</h1>
      <p class="lede">BSIT student at Torres Capitol College. I design the database, write the code and shape the screen, from a lost umbrella report to the moment it is returned.</p>
      <div class="btns">
        <a class="btn fill" href="#projects">See my projects</a>
        <a class="btn" href="#contact">Send a message</a>
      </div>
    </div>
    <div class="ticket-wrap">
      <article class="ticket" aria-label="Claim ticket with my details">
        <div class="head"><b>Claim ticket</b><small>Torres Capitol College</small></div>
        <div class="body">
          <img src="photo.webp" alt="Portrait of KC Faith B. Duerme in a navy blazer">
          <dl>
            <div><dt>Item</dt><dd>KC Faith B. Duerme</dd></div>
            <div><dt>Course</dt><dd>BSIT 2A, major in Entrepreneurship</dd></div>
            <div><dt>Currently building</dt><dd>Campus Lost &amp; Found System</dd></div>
          </dl>
        </div>
        <div class="stub">
          <div class="bars" aria-hidden="true"></div>
          <p>Return to: kcfaithduerme23@gmail.com</p>
        </div>
      </article>
    </div>
  </div>
</div>

<section id="about">
  <div class="wrap">
    <div class="sec-head"><h2>About me</h2></div>
    <div class="about">
      <div>
        <p>I’m a second year BSIT student, majoring in Entrepreneurship, at Torres Capitol College in Quezon, Bukidnon.</p>
        <p>I like practical problems: things people lose, forms people fill in, records people need to find. I enjoy turning them into working systems through web development, database design and system analysis.</p>
        <p>My goal is to keep growing as a developer and build tools that help my community.</p>
      </div>
      <ul class="timeline" aria-label="Education timeline">
        <li><b>Dean’s List</b><span>First semester, 2025–2026</span></li>
        <li><b>BSIT Seminar-Workshop</b><span>Certificate of Participation, April 29, 2026</span></li>
        <li><b>Expected graduation</b><span>April 2029, Torres Capitol College</span></li>
      </ul>
    </div>
  </div>
</section>

<section id="projects">
  <div class="wrap">
    <div class="sec-head">
      <h2>Projects</h2>
      <p>Three things I have built: a campus problem solved, a desktop system for managing staff, and one just for fun.</p>
    </div>

    <article class="project">
      <div>
        <h3>Campus Lost &amp; Found System</h3>
        <p class="role">Capstone project · Lead developer and system designer</p>
        <p>A web system where students and staff report lost items, browse found items and claim what belongs to them, so fewer things go unclaimed around campus.</p>
        <ul>
          <li>Report lost or found items with photos and details</li>
          <li>Search and filter by item type, location and date</li>
          <li>Admin approval and claim verification</li>
          <li>Survey module for user feedback</li>
        </ul>
        <dl class="facts">
          <div><dt>Built with</dt><dd>HTML/CSS, Python (Flask), SQLite, VS Code</dd></div>
          <div><dt>I learned</dt><dd>Requirements gathering, database design, writing questionnaires and working in a dev team</dd></div>
        </dl>
      </div>
      <div class="visual">
        <div class="screen" role="img" aria-label="Sample screen of the Lost and Found system listing found items">
          <div class="bar"><i></i><i></i><i></i><span>Campus Lost &amp; Found</span></div>
          <div class="find">Search items, places or dates</div>
          <div class="row"><div><b>Black umbrella</b><small>Library, 2nd floor</small></div><span class="pill">Found</span></div>
          <div class="row"><div><b>Blue tumbler</b><small>Canteen</small></div><span class="pill wait">Claim pending</span></div>
          <div class="row"><div><b>Student ID</b><small>Main gate</small></div><span class="pill ok">Returned</span></div>
        </div>
        <p class="caption">Sample items shown for illustration.</p>
      </div>
    </article>

    <article class="project flip">
      <div>
        <h3>EIS: Employee Information System</h3>
        <p class="role">Desktop application · Developer</p>
        <p>A Windows desktop system that keeps staff records, attendance, leave and payroll estimates in one place, with sign-in and permissions that depend on who is using it.</p>
        <ul>
          <li>Employee records with photos, search and editing</li>
          <li>Clock in and clock out with late detection</li>
          <li>Leave requests, balances and manager approval</li>
          <li>Monthly payroll estimate with SSS, PhilHealth, Pag-IBIG and withholding tax</li>
          <li>Admin, Manager and Viewer roles, audit log, CSV reports and daily backups</li>
        </ul>
        <dl class="facts">
          <div><dt>Built with</dt><dd>Python, Tkinter, SQLite, Pillow</dd></div>
          <div><dt>I learned</dt><dd>Password hashing and account lockout, role-based access, database transactions and moving an app from JSON files to SQLite</dd></div>
        </dl>
      </div>
      <div class="visual">
        <div class="screen eis" role="img" aria-label="Sample screen of the Employee Information System showing staff, attendance and leave">
          <div class="bar"><i></i><i></i><i></i><span>EIS · Employee Information System</span></div>
          <div class="find">Search by ID, name, department or position</div>
          <div class="row"><div><b>Ana Reyes</b><small>Software Developer</small></div><span class="pill ok">Clocked in</span></div>
          <div class="row"><div><b>Mark Bautista</b><small>Web Developer</small></div><span class="pill wait">Late</span></div>
          <div class="row"><div><b>Patricia Garcia</b><small>Annual leave, 3 days</small></div><span class="pill">Pending</span></div>
          <div class="row"><div><b>Salary</b><small>Visible to Admin and Manager only</small></div><span class="pill mute">Restricted</span></div>
        </div>
        <p class="caption">Sample records shown for illustration.</p>
      </div>
    </article>

    <article class="project">
      <div>
        <h3>Truth or Dare: Neon Party Spinner</h3>
        <p class="role">Desktop game · Developer</p>
        <p>Players spin a wheel to see whose turn it is, then pick Truth or Dare and get a random prompt.</p>
        <ul>
          <li>2 to 10 players with editable names and colors</li>
          <li>Spinner wheel, round counter and player carousel</li>
          <li>20 truth and 20 dare prompts</li>
          <li>Scoreboard that tracks truths and dares per player</li>
          <li>Layout that adapts to small screens</li>
        </ul>
        <dl class="facts">
          <div><dt>Built with</dt><dd>Python, Tkinter</dd></div>
        </dl>
      </div>
      <div class="visual">
        <div class="neon">
          <div class="wheel" id="wheel" role="button" tabindex="0" aria-label="Spin the wheel"></div>
          <p>Tap the wheel to spin</p>
        </div>
      </div>
    </article>
  </div>
</section>

<section id="skills">
  <div class="wrap">
    <div class="sec-head"><h2>Skills</h2></div>
    <dl class="skills">
      <div><dt>Programming</dt><dd>HTML/CSS, JavaScript, Python (Flask, Tkinter), Java, PHP, SQLite, MySQL</dd></div>
      <div><dt>Tools and platforms</dt><dd>VS Code, Git, Replit, Google Workspace, Microsoft Office, Canva</dd></div>
      <div><dt>Working style</dt><dd>Teamwork, documentation, technical writing, survey design, problem-solving</dd></div>
      <div><dt>Languages</dt><dd>English (proficient), Filipino/Tagalog (native)</dd></div>
    </dl>
  </div>
</section>

<section id="recognition">
  <div class="wrap">
    <div class="sec-head"><h2>Recognition</h2></div>
    <div class="recog">
      <div>
        <div class="item"><h3>Dean’s List</h3><p>First semester, 2025–2026, Torres Capitol College.</p></div>
        <div class="item"><h3>BSIT Seminar-Workshop 2026</h3><p>Certificate of Participation, held April 29, 2026. Theme: “Code + Communicate: IT Hard Skills and Soft Skills That Industry Demands.”</p></div>
      </div>
      <a href="cert.jpg" target="_blank" rel="noopener"><img class="cert" src="cert.jpg" alt="Certificate of Participation, BSIT Seminar-Workshop 2026, awarded to Duerme, KC Faith B."></a>
    </div>
  </div>
</section>

<section id="contact">
  <div class="wrap">
    <div class="sec-head">
      <h2>Get in touch</h2>
      <p>Have a question or a project idea? Send me a message.</p>
    </div>
    <div class="contact">
      <dl>
        <div><dt>Email</dt><dd><a href="mailto:kcfaithduerme23@gmail.com">kcfaithduerme23@gmail.com</a></dd></div>
        <div><dt>Phone</dt><dd><a href="tel:09916970189">09916970189</a></dd></div>
        <div><dt>Facebook</dt><dd>KC Faith B. Duerme</dd></div>
        <div><dt>Location</dt><dd>P-Maligaya, Salawagan, Quezon, Bukidnon</dd></div>
      </dl>
      <form id="cf">
        <label>Your name<input id="n" required autocomplete="name"></label>
        <label>Your email<input id="e" type="email" required autocomplete="email"></label>
        <label>Message<textarea id="m" required></textarea></label>
        <button class="btn fill" type="submit">Send message</button>
      </form>
    </div>
  </div>
</section>

</main>

<footer>
  <div class="wrap"><span>© 2026 KC Faith B. Duerme</span><span>BSIT, Torres Capitol College</span></div>
</footer>

<script>
(function(){
  /* highlight the nav link of the section in view */
  var links=document.querySelectorAll('nav a');
  var map={};links.forEach(function(a){map[a.getAttribute('href').slice(1)]=a});
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){
      es.forEach(function(en){
        if(en.isIntersecting){links.forEach(function(a){a.removeAttribute('aria-current')});
          var a=map[en.target.id];if(a)a.setAttribute('aria-current','true')}
      })
    },{rootMargin:'-45% 0px -50% 0px'});
    Object.keys(map).forEach(function(id){var s=document.getElementById(id);if(s)io.observe(s)});
  }

  /* spin the wheel on tap or Enter/Space */
  var w=document.getElementById('wheel'),deg=0;
  function spin(){deg+=1080+Math.floor(Math.random()*360);w.style.transform='rotate('+deg+'deg)'}
  w.addEventListener('click',spin);
  w.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();spin()}});

  /* contact form opens the visitor's email app */
  document.getElementById('cf').addEventListener('submit',function(ev){
    ev.preventDefault();
    var n=document.getElementById('n').value,e=document.getElementById('e').value,m=document.getElementById('m').value;
    var s=encodeURIComponent('Portfolio message from '+n);
    var b=encodeURIComponent(m+'\n\nFrom: '+n+' ('+e+')');
    location.href='mailto:kcfaithduerme23@gmail.com?subject='+s+'&body='+b;
  });
})();
</script>
</body>
</html>
'''


def main():
    try:
        base = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        base = os.getcwd()
    site = os.path.join(base, "portfolio_site")
    os.makedirs(site, exist_ok=True)

    missing = [f for f in ("photo.webp", "cert.jpg")
               if not os.path.exists(os.path.join(site, f))]
    if missing:
        print("Missing in portfolio_site:", ", ".join(missing))
        print("Run your original portfolio script once first, then run this file.")

    with open(os.path.join(site, "index.html"), "w", encoding="utf-8") as f:
        f.write(HTML)

    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=site, **kwargs)

        def log_message(self, *args):
            pass

    socketserver.TCPServer.allow_reuse_address = True
    server = None
    for port in range(8000, 8011):
        try:
            server = socketserver.ThreadingTCPServer(("127.0.0.1", port), Handler)
            break
        except OSError:
            continue
    if server is None:
        print("Could not start the server. Close other running scripts and try again.")
        return

    # Chrome treats any *.localhost name as this phone, so this works offline.
    url = "http://kcfaithduerme-portfolio.localhost:%d/" % port
    backup = "http://127.0.0.1:%d/" % port
    print("Portfolio is running at:", url)
    print("If that address does not open, use:", backup)
    print("Files saved in:", site)
    threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()