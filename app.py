import streamlit as st
from datetime import datetime, timedelta
import time

# Page config
st.set_page_config(
    page_title="ГеоОлімп — Геометрична олімпіада",
    page_icon="△",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    .stApp {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(180deg, #f8f9fa 0%, #ffffff 100%);
    }

    /* Hero */
    .hero-container {
        background: linear-gradient(135deg, #1a3a5c 0%, #0d1f33 100%);
        border-radius: 20px;
        padding: 3rem 2rem;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }

    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
    }

    .hero-title span {
        color: #c9a227;
    }

    .hero-subtitle {
        font-size: 1.15rem;
        color: rgba(255,255,255,0.8);
        margin-bottom: 1.5rem;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }

    .hero-badges {
        display: flex;
        gap: 0.8rem;
        justify-content: center;
        flex-wrap: wrap;
        margin-bottom: 1.5rem;
    }

    .hero-badge {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        padding: 0.4rem 1rem;
        border-radius: 50px;
        font-size: 0.85rem;
        border: 1px solid rgba(255,255,255,0.15);
        color: white;
    }

    /* Countdown */
    .countdown-container {
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        text-align: center;
        margin-top: -2rem;
        position: relative;
        z-index: 2;
        margin-bottom: 2rem;
    }

    .countdown-label {
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: #718096;
        margin-bottom: 0.8rem;
    }

    .countdown-grid {
        display: flex;
        justify-content: center;
        gap: 2rem;
    }

    .countdown-item {
        text-align: center;
    }

    .countdown-number {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1a3a5c;
        line-height: 1;
    }

    .countdown-text {
        font-size: 0.75rem;
        color: #718096;
        text-transform: uppercase;
        margin-top: 0.2rem;
    }

    /* Cards */
    .info-card {
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 2px 12px rgba(0,0,0,0.06);
        border: 1px solid #e2e8f0;
        height: 100%;
        transition: transform 0.3s;
    }

    .info-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.1);
    }

    .card-icon {
        width: 48px;
        height: 48px;
        background: linear-gradient(135deg, #1a3a5c, #2c5282);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.3rem;
        margin-bottom: 0.8rem;
    }

    .card-title {
        font-size: 1rem;
        font-weight: 700;
        color: #1a3a5c;
        margin-bottom: 0.4rem;
    }

    .card-text {
        color: #718096;
        font-size: 0.9rem;
        line-height: 1.6;
    }

    /* Section titles */
    .section-title {
        font-size: 1.8rem;
        color: #1a3a5c;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.3rem;
    }

    .section-subtitle {
        text-align: center;
        color: #718096;
        margin-bottom: 2rem;
        font-size: 1rem;
    }

    /* Timeline */
    .timeline-item {
        display: flex;
        gap: 1.5rem;
        margin-bottom: 1.5rem;
        padding-left: 1.5rem;
        border-left: 3px solid #e2e8f0;
        position: relative;
    }

    .timeline-item::before {
        content: '';
        position: absolute;
        left: -8px;
        top: 0;
        width: 14px;
        height: 14px;
        background: #c9a227;
        border-radius: 50%;
        border: 3px solid white;
        box-shadow: 0 0 0 3px #c9a227;
    }

    .timeline-item.highlight::before {
        background: #38a169;
        box-shadow: 0 0 0 3px #38a169;
    }

    .timeline-date {
        font-size: 0.8rem;
        color: #c9a227;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .timeline-title {
        font-size: 1.05rem;
        color: #1a3a5c;
        font-weight: 700;
        margin: 0.2rem 0;
    }

    .timeline-desc {
        font-size: 0.9rem;
        color: #718096;
    }

    /* Archive cards */
    .archive-card {
        background: white;
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 2px 12px rgba(0,0,0,0.06);
        border: 1px solid #e2e8f0;
        height: 100%;
    }

    .archive-header {
        background: linear-gradient(135deg, #1a3a5c, #2c5282);
        color: white;
        padding: 1.2rem;
        position: relative;
    }

    .archive-year {
        font-size: 1.8rem;
        font-weight: 800;
        opacity: 0.3;
        position: absolute;
        top: 0.3rem;
        right: 1rem;
    }

    .archive-header h4 {
        margin: 0;
        font-size: 1rem;
        position: relative;
        z-index: 1;
    }

    .archive-body {
        padding: 1.2rem;
    }

    .archive-stats {
        display: flex;
        gap: 1.5rem;
        margin-bottom: 1rem;
    }

    .archive-stat {
        text-align: center;
    }

    .archive-stat-num {
        font-size: 1.2rem;
        font-weight: 700;
        color: #1a3a5c;
    }

    .archive-stat-lbl {
        font-size: 0.7rem;
        color: #718096;
        text-transform: uppercase;
    }

    /* Table */
    .results-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.9rem;
    }

    .results-table th {
        background: linear-gradient(135deg, #1a3a5c, #2c5282);
        color: white;
        padding: 0.8rem 1rem;
        text-align: left;
        font-weight: 600;
    }

    .results-table td {
        padding: 0.7rem 1rem;
        border-bottom: 1px solid #e2e8f0;
    }

    .results-table tr:hover {
        background: #f7fafc;
    }

    .rank-cell {
        font-weight: 800;
        color: #c9a227;
        font-size: 1.1rem;
    }

    .score-cell {
        font-weight: 700;
        color: #1a3a5c;
    }

    /* Form */
    .form-container {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 4px 24px rgba(0,0,0,0.08);
        max-width: 700px;
        margin: 0 auto;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #1a3a5c, #2c5282) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.7rem 2rem !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        width: 100% !important;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(26,58,92,0.3) !important;
    }

    /* Footer */
    .footer {
        background: #1a3a5c;
        color: white;
        padding: 2rem;
        border-radius: 16px;
        margin-top: 3rem;
        text-align: center;
    }

    .footer-text {
        color: rgba(255,255,255,0.7);
        font-size: 0.9rem;
    }

    /* Portrait */
    .portrait-card {
        background: linear-gradient(135deg, #1a3a5c, #2c5282);
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 20px 60px rgba(26,58,92,0.3);
    }

    .portrait-emoji {
        font-size: 4rem;
        margin-bottom: 1rem;
    }

    .portrait-name {
        font-size: 1.1rem;
        font-weight: 700;
    }

    .portrait-role {
        font-size: 0.85rem;
        opacity: 0.8;
        margin-top: 0.3rem;
    }

    /* Stats boxes */
    .stat-box {
        text-align: center;
        padding: 1rem;
        background: white;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }

    .stat-box-num {
        font-size: 2rem;
        font-weight: 800;
        color: #1a3a5c;
    }

    .stat-box-lbl {
        font-size: 0.8rem;
        color: #718096;
    }

    /* Hide streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
    }

    .stTabs [data-baseweb="tab"] {
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        border-radius: 8px 8px 0 0;
    }

    .stTabs [aria-selected="true"] {
        background: #1a3a5c !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# ============ NAVIGATION ============
page = st.session_state.get("page", "home")

# Top navigation
nav_cols = st.columns(6)
nav_items = [
    ("🏠 Головна", "home"),
    ("📖 Про олімпіаду", "about"),
    ("📅 Розклад", "schedule"),
    ("📚 Архів", "archive"),
    ("🏆 Результати", "results"),
    ("📝 Реєстрація", "register")
]

for i, (label, key) in enumerate(nav_items):
    if nav_cols[i].button(label, key=f"nav_{key}", use_container_width=True,
                          type="primary" if page == key else "secondary"):
        st.session_state.page = key
        st.rerun()

st.markdown("<hr style='margin: 0.5rem 0 1.5rem 0; border: none; border-top: 1px solid #e2e8f0;'>", unsafe_allow_html=True)

# ============ HOME PAGE ============
if page == "home":
    # Hero
    st.markdown("""
    <div class="hero-container">
        <div class="hero-title">Геометрична олімпіада <span>«ГеоОлімп»</span></div>
        <div class="hero-subtitle">Щорічне міжнародне змагання для поціновувачів красивих геометричних задач. Перевір свої сили разом із найкращими!</div>
        <div class="hero-badges">
            <span class="hero-badge">📅 Листопад 2026</span>
            <span class="hero-badge">🌐 Онлайн</span>
            <span class="hero-badge">🎯 8–11 класи</span>
            <span class="hero-badge">🏆 5 задач · 4 години</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Countdown
    olympiad_date = datetime(2026, 11, 15, 10, 0, 0)
    now = datetime.now()
    diff = olympiad_date - now

    if diff.total_seconds() > 0:
        days = diff.days
        hours = diff.seconds // 3600
        minutes = (diff.seconds % 3600) // 60
        seconds = diff.seconds % 60
    else:
        days = hours = minutes = seconds = 0

    st.markdown(f"""
    <div class="countdown-container">
        <div class="countdown-label">До початку X ГеоОлімпу залишилось</div>
        <div class="countdown-grid">
            <div class="countdown-item">
                <div class="countdown-number">{days:02d}</div>
                <div class="countdown-text">днів</div>
            </div>
            <div class="countdown-item">
                <div class="countdown-number">{hours:02d}</div>
                <div class="countdown-text">годин</div>
            </div>
            <div class="countdown-item">
                <div class="countdown-number">{minutes:02d}</div>
                <div class="countdown-text">хвилин</div>
            </div>
            <div class="countdown-item">
                <div class="countdown-number">{seconds:02d}</div>
                <div class="countdown-text">секунд</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Info cards
    st.markdown('<div class="section-title">Про олімпіаду</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Все, що потрібно знати про участь у змаганні</div>', unsafe_allow_html=True)

    cards = [
        ("📅", "Дата проведення", "Олімпіада відбудеться у листопаді 2026 року. Точна дата буде оголошена за місяць до старту."),
        ("👥", "Хто може брати участь", "Учні 8, 9, 10 та 11 класів загальноосвітніх шкіл, гімназій та ліцеїв з усього світу."),
        ("💻", "Формат змагання", "Повністю онлайн. 5 геометричних задач, 4 години на розв'язання. Кожна задача оцінюється від 0 до 7 балів."),
        ("📝", "Реєстрація", "Попередня реєстрація не обов'язкова. У день олімпіади відкриється форма для надсилання розв'язків у форматі PDF."),
        ("🌍", "Мови", "Розв'язки приймаються українською та англійською мовами. Умови задач будуть доступні обома мовами."),
        ("🏅", "Нагородження", "Учасники отримують дипломи I–III ступеня та сертифікати участі. Переможці — спеціальні призи."),
    ]

    for i in range(0, len(cards), 3):
        cols = st.columns(3)
        for j, (icon, title, text) in enumerate(cards[i:i+3]):
            with cols[j]:
                st.markdown(f"""
                <div class="info-card">
                    <div class="card-icon">{icon}</div>
                    <div class="card-title">{title}</div>
                    <div class="card-text">{text}</div>
                </div>
                """, unsafe_allow_html=True)

# ============ ABOUT PAGE ============
elif page == "about":
    st.markdown("""
    <div class="hero-container" style="padding: 2.5rem 2rem;">
        <div class="hero-title" style="font-size: 2.2rem;">Про <span>ГеоОлімп</span></div>
        <div class="hero-subtitle">Історія, місія та натхнення нашої олімпіади</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        <h2 style="color: #1a3a5c; margin-bottom: 1rem;">Історія олімпіади</h2>
        <p style="color: #718096; line-height: 1.8; margin-bottom: 1rem;">
        Геометрична олімпіада «ГеоОлімп» була заснована у 2018 році групою ентузіастів-математиків з метою популяризації геометрії серед школярів. За роки існування олімпіада зібрала тисячі учасників з понад 30 країн світу.
        </p>
        <p style="color: #718096; line-height: 1.8; margin-bottom: 1rem;">
        Олімпіада названа на честь видатного українського педагога-математика, автора сотень олімпіадних задач, чиї роботи надихають нові покоління математиків.
        </p>
        <p style="color: #718096; line-height: 1.8;">
        Складність задач відповідає рівню національних олімпіад, що робить «ГеоОлімп» чудовою підготовкою до серйозніших змагань.
        </p>
        """, unsafe_allow_html=True)

        # Stats
        stats = [("9", "років існування"), ("30+", "країн-учасниць"), ("5000+", "учасників")]
        stat_cols = st.columns(3)
        for i, (num, lbl) in enumerate(stats):
            with stat_cols[i]:
                st.markdown(f"""
                <div class="stat-box">
                    <div class="stat-box-num">{num}</div>
                    <div class="stat-box-lbl">{lbl}</div>
                </div>
                """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="portrait-card">
            <div class="portrait-emoji">👤</div>
            <div class="portrait-name">Професор Геометрій</div>
            <div class="portrait-role">Засновник олімпіади</div>
            <div class="portrait-role" style="margin-top:0.5rem; font-size:0.75rem;">Автор 200+ олімпіадних задач</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Rules
    st.markdown('<div class="section-title">Правила олімпіади</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Ознайомтесь із правилами перед участю</div>', unsafe_allow_html=True)

    rules = [
        ("1️⃣", "Формат змагання", "Учасникам пропонується 5 геометричних задач різного рівня складності. На розв'язання відводиться рівно 4 години (240 хвилин). Кожна задача оцінюється від 0 до 7 балів за шкалою ММО."),
        ("2️⃣", "Подання розв'язків", "Розв'язки записуються письмово на папері, потім скануються або фотографуються та надсилаються у форматі PDF через форму на сайті. Розв'язки мають бути чіткими, зрозумілими та повними."),
        ("3️⃣", "Заборонені інструменти", "Під час олімпіади заборонено використовувати будь-які електронні пристрої (крім пристрою для відправки розв'язків), програмне забезпечення для побудови геометричних фігур, спілкуватися з іншими учасниками або шукати розв'язки в Інтернеті."),
        ("4️⃣", "Оцінювання та нагородження", "Розв'язки перевіряються журі протягом 2–3 тижнів після олімпіади. Учасники, які наберуть 28+ балів, отримують диплом I ступеня; 21–27 — II ступеня; 14–20 — III ступеня."),
    ]

    for icon, title, text in rules:
        st.markdown(f"""
        <div class="info-card" style="margin-bottom: 1rem;">
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
                <div style="font-size: 1.5rem; flex-shrink: 0;">{icon}</div>
                <div>
                    <div class="card-title">{title}</div>
                    <div class="card-text">{text}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ============ SCHEDULE PAGE ============
elif page == "schedule":
    st.markdown("""
    <div class="hero-container" style="padding: 2.5rem 2rem;">
        <div class="hero-title" style="font-size: 2.2rem;">Розклад <span>ГеоОлімпу 2026</span></div>
        <div class="hero-subtitle">Ключові дати та етапи підготовки до змагання</div>
    </div>
    """, unsafe_allow_html=True)

    timeline = [
        ("1 вересня 2026", "Відкриття реєстрації", "Починається прийом заявок на участь у X ГеоОлімпі. Реєстрація триватиме до дня олімпіади.", False),
        ("15 жовтня 2026", "Публікація зразкових задач", "На сайті з'являться 3 тренувальні задачі для ознайомлення з форматом та складністю олімпіади.", False),
        ("1 листопада 2026", "Оголошення точної дати", "Оголошується точна дата та час проведення олімпіади. Учасники отримують нагадування на email.", False),
        ("15 листопада 2026", "🎯 День олімпіади", "О 10:00 за київським часом стартують змагання. Тривалість — 4 години. Умови задач публікуються на сайті.", True),
        ("30 листопада 2026", "Завершення перевірки", "Журі завершує перевірку всіх розв'язків. Попередні результати публікуються на сайті.", False),
        ("10 грудня 2026", "Оголошення результатів", "Фінальні результати, розв'язки задач та нагородження переможців. Відправка дипломів учасникам.", False),
    ]

    for date, title, desc, highlight in timeline:
        highlight_class = "highlight" if highlight else ""
        st.markdown(f"""
        <div class="timeline-item {highlight_class}">
            <div>
                <div class="timeline-date">{date}</div>
                <div class="timeline-title">{title}</div>
                <div class="timeline-desc">{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ============ ARCHIVE PAGE ============
elif page == "archive":
    st.markdown("""
    <div class="hero-container" style="padding: 2.5rem 2rem;">
        <div class="hero-title" style="font-size: 2.2rem;">Архів <span>задач</span></div>
        <div class="hero-subtitle">Задачі та розв'язки минулих олімпіад для підготовки</div>
    </div>
    """, unsafe_allow_html=True)

    archives = [
        ("IX", "ГеоОлімп 2025", 5, 847, 32),
        ("VIII", "ГеоОлімп 2024", 5, 723, 28),
        ("VII", "ГеоОлімп 2023", 5, 651, 25),
        ("VI", "ГеоОлімп 2022", 5, 534, 22),
        ("V", "ГеоОлімп 2021", 5, 412, 18),
        ("IV", "ГеоОлімп 2020", 5, 389, 15),
    ]

    for i in range(0, len(archives), 3):
        cols = st.columns(3)
        for j, (roman, name, problems, participants, countries) in enumerate(archives[i:i+3]):
            with cols[j]:
                st.markdown(f"""
                <div class="archive-card">
                    <div class="archive-header">
                        <div class="archive-year">{roman}</div>
                        <h4>{name}</h4>
                    </div>
                    <div class="archive-body">
                        <div class="archive-stats">
                            <div class="archive-stat">
                                <div class="archive-stat-num">{problems}</div>
                                <div class="archive-stat-lbl">задач</div>
                            </div>
                            <div class="archive-stat">
                                <div class="archive-stat-num">{participants}</div>
                                <div class="archive-stat-lbl">учасників</div>
                            </div>
                            <div class="archive-stat">
                                <div class="archive-stat-num">{countries}</div>
                                <div class="archive-stat-lbl">країни</div>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                c1, c2, c3 = st.columns(3)
                with c1:
                    st.button("📄 Умови", key=f"prob_{roman}", use_container_width=True)
                with c2:
                    st.button("✓ Розв'язки", key=f"sol_{roman}", use_container_width=True)
                with c3:
                    st.button("🏆 Результати", key=f"res_{roman}", use_container_width=True)

# ============ RESULTS PAGE ============
elif page == "results":
    st.markdown("""
    <div class="hero-container" style="padding: 2.5rem 2rem;">
        <div class="hero-title" style="font-size: 2.2rem;">Результати <span>олімпіад</span></div>
        <div class="hero-subtitle">Рейтинги та статистика попередніх змагань</div>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["ГеоОлімп 2025", "ГеоОлімп 2024", "ГеоОлімп 2023", "Статистика"])

    with tab1:
        results_2025 = [
            (1, "Олександр Ковальчук", "🇺🇦 Україна", 11, 7, 7, 7, 7, 7, 35, "🥇 Золото"),
            (2, "Марія Новак", "🇵🇱 Польща", 11, 7, 7, 7, 7, 6, 34, "🥇 Золото"),
            (3, "Іван Петренко", "🇺🇦 Україна", 10, 7, 7, 7, 6, 7, 34, "🥇 Золото"),
            (4, "Анна Вішневська", "🇵🇱 Польща", 10, 7, 7, 6, 7, 6, 33, "🥈 Срібло"),
            (5, "Давид Козлов", "🇨🇿 Чехія", 11, 7, 7, 7, 5, 6, 32, "🥈 Срібло"),
            (6, "Софія Мельник", "🇺🇦 Україна", 9, 7, 6, 7, 7, 4, 31, "🥈 Срібло"),
            (7, "Томаш Новотни", "🇸🇰 Словаччина", 11, 7, 7, 5, 6, 5, 30, "🥉 Бронза"),
            (8, "Єва Горват", "🇭🇺 Угорщина", 10, 7, 5, 7, 6, 4, 29, "🥉 Бронза"),
        ]

        html = '<table class="results-table"><thead><tr><th>Місце</th><th>Учасник</th><th>Країна</th><th>Клас</th><th>З1</th><th>З2</th><th>З3</th><th>З4</th><th>З5</th><th>Усього</th><th>Нагорода</th></tr></thead><tbody>'
        for r in results_2025:
            html += f'<tr><td class="rank-cell">{r[0]}</td><td><strong>{r[1]}</strong></td><td>{r[2]}</td><td>{r[3]}</td><td>{r[4]}</td><td>{r[5]}</td><td>{r[6]}</td><td>{r[7]}</td><td>{r[8]}</td><td class="score-cell">{r[9]}</td><td>{r[10]}</td></tr>'
        html += '</tbody></table>'
        st.markdown(html, unsafe_allow_html=True)

    with tab2:
        results_2024 = [
            (1, "Павло Шевченко", "🇺🇦 Україна", 11, 35, "🥇 Золото"),
            (2, "Катаржина Вісньовська", "🇵🇱 Польща", 11, 33, "🥇 Золото"),
            (3, "Андрій Бондаренко", "🇺🇦 Україна", 10, 32, "🥈 Срібло"),
            (4, "Мартін Новак", "🇨🇿 Чехія", 11, 30, "🥈 Срібло"),
            (5, "Олена Кравченко", "🇺🇦 Україна", 9, 28, "🥉 Бронза"),
        ]
        html = '<table class="results-table"><thead><tr><th>Місце</th><th>Учасник</th><th>Країна</th><th>Клас</th><th>Усього</th><th>Нагорода</th></tr></thead><tbody>'
        for r in results_2024:
            html += f'<tr><td class="rank-cell">{r[0]}</td><td><strong>{r[1]}</strong></td><td>{r[2]}</td><td>{r[3]}</td><td class="score-cell">{r[4]}</td><td>{r[5]}</td></tr>'
        html += '</tbody></table>'
        st.markdown(html, unsafe_allow_html=True)

    with tab3:
        results_2023 = [
            (1, "Максим Грищенко", "🇺🇦 Україна", 11, 34, "🥇 Золото"),
            (2, "Зузана Новакова", "🇸🇰 Словаччина", 11, 31, "🥈 Срібло"),
            (3, "Дмитро Сидоренко", "🇺🇦 Україна", 10, 29, "🥉 Бронза"),
        ]
        html = '<table class="results-table"><thead><tr><th>Місце</th><th>Учасник</th><th>Країна</th><th>Клас</th><th>Усього</th><th>Нагорода</th></tr></thead><tbody>'
        for r in results_2023:
            html += f'<tr><td class="rank-cell">{r[0]}</td><td><strong>{r[1]}</strong></td><td>{r[2]}</td><td>{r[3]}</td><td class="score-cell">{r[4]}</td><td>{r[5]}</td></tr>'
        html += '</tbody></table>'
        st.markdown(html, unsafe_allow_html=True)

    with tab4:
        stats_cards = [
            ("📊", "Учасники за роками", "2020: 389 | 2021: 412 | 2022: 534 | 2023: 651 | 2024: 723 | 2025: 847", "↑ Зростання +118% за 5 років"),
            ("🌍", "Географія учасників", "Топ-5 країн (2025): Україна (45%), Польща (18%), Чехія (8%), Словаччина (6%), Угорщина (5%)", ""),
            ("🏅", "Розподіл нагород (2025)", "🥇 Золото: 12 учасників (28+ балів)\n🥈 Срібло: 34 учасники (21–27 балів)\n🥉 Бронза: 89 учасників (14–20 балів)", ""),
            ("📈", "Середній бал", "Середній результат учасника: 16.4 бали\nМедіана: 14 бали\nНайскладніша задача: №3 (середній бал 3.2)", ""),
        ]

        for icon, title, text, extra in stats_cards:
            st.markdown(f"""
            <div class="info-card" style="margin-bottom: 1rem;">
                <div style="display: flex; gap: 1rem; align-items: flex-start;">
                    <div class="card-icon">{icon}</div>
                    <div>
                        <div class="card-title">{title}</div>
                        <div class="card-text">{text.replace(chr(10), '<br>')}</div>
                        {f'<div style="color: #38a169; font-weight: 600; margin-top: 0.5rem;">{extra}</div>' if extra else ''}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# ============ REGISTER PAGE ============
elif page == "register":
    st.markdown("""
    <div class="hero-container" style="padding: 2.5rem 2rem;">
        <div class="hero-title" style="font-size: 2.2rem;">Реєстрація на <span>ГеоОлімп 2026</span></div>
        <div class="hero-subtitle">Заповніть форму, щоб отримати нагадування про олімпіаду</div>
    </div>
    """, unsafe_allow_html=True)

    with st.form("registration_form"):
        col1, col2 = st.columns(2)
        with col1:
            fname = st.text_input("Ім'я *", placeholder="Ваше ім'я")
        with col2:
            lname = st.text_input("Прізвище *", placeholder="Ваше прізвище")

        email = st.text_input("Електронна пошта *", placeholder="example@email.com")
        st.caption("На цю адресу надійде нагадування про олімпіаду")

        col3, col4 = st.columns(2)
        with col3:
            country = st.selectbox("Країна *", ["", "🇺🇦 Україна", "🇵🇱 Польща", "🇨🇿 Чехія", "🇸🇰 Словаччина", "🇭🇺 Угорщина", "🇷🇴 Румунія", "🇧🇬 Болгарія", "Інша країна"])
        with col4:
            city = st.text_input("Місто *", placeholder="Ваше місто")

        col5, col6 = st.columns(2)
        with col5:
            school = st.text_input("Навчальний заклад *", placeholder="Назва школи / ліцею")
        with col6:
            grade = st.selectbox("Клас *", ["", "8 клас", "9 клас", "10 клас", "11 клас"])

        lang = st.selectbox("Мова розв'язків *", ["", "Українська", "English"])
        comments = st.text_area("Додаткові коментарі (необов'язково)", placeholder="Наприклад: особливі потреби, питання щодо олімпіади...")

        submitted = st.form_submit_button("✓ Підтвердити реєстрацію")

        if submitted:
            if fname and lname and email and country and city and school and grade and lang:
                st.success("✅ Реєстрація успішна! На вашу пошту надійде нагадування про олімпіаду.")
                st.balloons()
            else:
                st.error("❌ Будь ласка, заповніть всі обов'язкові поля (позначені *)")

    st.caption("Натискаючи кнопку, ви погоджуєтесь з правилами олімпіади")

# ============ FOOTER ============
st.markdown("""
<div class="footer">
    <div style="font-size: 1.2rem; font-weight: 700; margin-bottom: 0.5rem;">🟨 ГеоОлімп</div>
    <div class="footer-text">
        Геометрична олімпіада «ГеоОлімп» — щорічне міжнародне змагання для школярів, які полюбляють геометрію.<br>
        📧 info@geo-olymp.org | 🌐 geo-olymp.org<br><br>
        © 2026 ГеоОлімп. Всі права захищено.
    </div>
</div>
""", unsafe_allow_html=True)
