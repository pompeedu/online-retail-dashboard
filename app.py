import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio

# ---------------------------------------------
# НАСТРОЙКИ СТРАНИЦЫ
# ---------------------------------------------
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="Интерактивный дашборд",
    layout="wide",
    page_icon=":bar_chart:",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------
# УПРАВЛЕНИЕ СОСТОЯНИЕМ ПРИЛОЖЕНИЯ
# ---------------------------------------------
# Инициализация состояния входа
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ---------------------------------------------
# ГЛАВНАЯ СТРАНИЦА (LANDING PAGE)
# ---------------------------------------------
if not st.session_state.authenticated:
    # Заголовок
    st.title("📊 Дашборд онлайн-ритейла")
    st.markdown("Интерактивный анализ продаж, клиентов и бизнес-метрик")
    st.markdown("---")

    # Основной контент в две колонки 
    col_left, col_right = st.columns([2, 1])

    with col_left:
        # Краткое описание
        st.markdown("""
        ##### **О проекте:**  
        Дашборд для анализа транзакций онлайн-магазина с фокусом на ключевые 
        бизнес-метрики: выручка, активность клиентов, география продаж и возвраты.
        """)

        # Основные возможности 
        st.markdown("""
        ##### **Что умеет:**
        - 📈 Ключевые метрики на одном экране
        - 🎯 Интерактивные графики и фильтры
        - 🌍 Географический анализ продаж
        - 📊 Анализ возвратов и проблемных зон
        - 📥 Экспорт данных в CSV
        """)

        st.markdown("##### **Спойлеры:**")

        with st.expander("📖 Подробнее о функциональности"):
            st.markdown("""
            ### Детальный обзор возможностей:
            
            **Аналитические блоки:**
            - **Ключевые метрики**: Общее количество продаж, выручка, средний чек, 
              уникальные клиенты, сумма возвратов
            - **Анализ продаж**: ТОП-20 товаров по выручке, динамика продаж по дням, 
              активность клиентов
            - **География**: Выручка по странам, ТОП-10 стран (с UK и без UK)
            - **Возвраты**: Динамика возвратов по времени, проблемные товары
            
            **Фильтрация:**
            - Диапазон дат (от/до)
            - Страны (множественный выбор)
            - ID клиентов
            - Код товара (StockCode)
            - Название товара (Description)
            
            **Особенности:**
            - ⚡ Оптимизированная работа с большими данными (кэширование)
            - 🎨 Кастомная тёмная тема для комфортного просмотра
            - 📱 Адаптивный дизайн (работает на всех устройствах)
            - 🔄 Реактивное обновление при изменении фильтров
            """)

        with st.expander("🛠 Технологии и стек"):
            st.markdown("""
            **Используемые технологии:**
            - **Python 3.9+** — основной язык разработки
            - **Streamlit** — фреймворк для веб-интерфейса
            - **Pandas** — обработка и анализ данных
            - **NumPy** — численные вычисления
            - **Plotly** — интерактивная визуализация
            
            **Архитектурные решения:**
            - Session State для управления состоянием
            - Кэширование данных и графиков
            - Отложенный рендеринг для оптимизации
            - Модульная структура кода
            """)

        with st.expander("💼 Для кого этот проект?"):
            st.markdown("""
            Этот дашборд — **демонстрация навыков** для портфолио, но подобные решения 
            я могу адаптировать под реальные бизнес-задачи:
            
            ✅ **Интернет-магазины** — анализ продаж, клиентов, товаров  
            ✅ **Маркетинговые агентства** — отчёты для клиентов  
            ✅ **Малый и средний бизнес** — простая аналитика без дорогих BI-систем  
            ✅ **Стартапы** — MVP дашбордов для инвесторов  
            ✅ **E-commerce проекты** — мониторинг KPI в реальном времени
            
            **Преимущества такого подхода:**
            - 🚀 Быстрая разработка (5-7 дней)
            - 💰 Доступная стоимость (от 15,000₽)
            - 🔧 Легко адаптируется под любые данные
            - 📊 Современный и понятный интерфейс
            """)

    with col_right:
        st.markdown("### ")
        st.markdown("### ")
        
        if st.button("🚀 Запустить дашборд", use_container_width=True, type="primary"):
            st.session_state.authenticated = True
            st.rerun()
        
        st.markdown("---")
        
        st.markdown("""
        <div class="contact-card">
            <h4>📩 Контакты</h4>
            <p><b>Telegram:</b><br>
                <a href='https://t.me/pompeedu' target='_blank'>
                    @pompeedu
                </a>
            </p>
            <p><b>Email:</b><br>
                <a href='mailto:firuzjonkurbonov735700@gmail.com' target='_blank'>
                    firuzjonkurbonov735700@gmail.com
                </a>
            </p>
            <p class="contact-hint">💡 Открыт для заказов и сотрудничества</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### ")
        
        st.markdown("""
        <div class="stat-card">
            <p><b>Технические характеристики:</b></p>
            <p>📊 541,909 транзакций</p>
            <p>🌍 38 стран</p>
            <p>🛍️ 4,070 товаров</p>
            <p>📅 Период: 2010-2011</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div class="landing-footer">
        <p>Разработано как демонстрационный проект для портфолио</p>
        <p>Готов создать аналогичное решение для вашего бизнеса</p>
    </div>
    """, unsafe_allow_html=True)

    st.stop()

# ---------------------------------------------
# ОСНОВНОЙ ДАШБОРД
# ---------------------------------------------
st.title("📊 Интерактивный дашборд онлайн-ритейла")
st.markdown("##### Чистый и удобный дашборд.")

# ---------------------------------------------
# ЗАГРУЗКА ДАННЫХ
# ---------------------------------------------

@st.cache_data(show_spinner="Загружаем данные...")
def load_data(file):
    return pd.read_csv(file, encoding="latin1")

df = load_data("Online_Retail.csv")

# ---------------------------------------------
# ОЧИСТКА ДАННЫХ
# ---------------------------------------------

EXCLUDED_DESCRIPTIONS = [
    "AMAZON FEE",
    "MANUAL",
    "ADJUST",
    "FEE",
    "C2",
    "POSTAGE",
    "BANK CHARGES"
]

@st.cache_data(show_spinner="Полируем датасет...")
def cleaning(df: pd.DataFrame, max_quantity, max_price) -> pd.DataFrame:
    df = df.copy()
    df['OriginalQuantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
    df = df.drop_duplicates()
    df = df.dropna(subset=['InvoiceNo'])
    
    df['InvoiceNo'] = df['InvoiceNo'].astype(str)
    df['IsCancelled'] = df['InvoiceNo'].str.startswith('C')
    df['PureInvoiceNo'] = df['InvoiceNo'].str.replace('C','',regex=False)
    
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
    df.loc[df['Quantity'] <= 0, 'Quantity'] = np.nan
    df.loc[df['Quantity'] > max_quantity, 'Quantity'] = np.nan
    
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
    
    df['UnitPrice'] = pd.to_numeric(df['UnitPrice'], errors='coerce')
    df.loc[df['UnitPrice'] <= 0, 'UnitPrice'] = np.nan
    df.loc[df['UnitPrice'] > max_price, 'UnitPrice'] = np.nan
    
    df['CustomerID'] = pd.to_numeric(df['CustomerID'], errors='coerce')
    df['CustomerID'] = df['CustomerID'].astype('Int64')
    df['CustomerID_filled'] = df['CustomerID'].astype(str)
    df.loc[df['CustomerID'].isna(), 'CustomerID_filled'] = "Неизвестный клиент"
    
    df['Country'] = df['Country'].astype(str).str.strip().str.title()
    
    df = df[(~df['Description'].isin(EXCLUDED_DESCRIPTIONS)) &
            (~df['Description'].str.upper().str.contains("|".join(EXCLUDED_DESCRIPTIONS), na=False))] 
    
    return df

df_clean = cleaning(df, 10000, 5000)

# ---------------------------------------------
# САЙДБАР ФИЛЬТРЫ
# ---------------------------------------------

def multiselect_with_all(label, options, key, all_label="Все"):
    """Мультиселект с опцией 'Все' - правильная инициализация"""
    opts = [all_label] + list(options)
    
    # Инициализация: если ключа нет в session_state, устанавливаем "Все"
    if key not in st.session_state:
        st.session_state[key] = [all_label]
    
    # Виджет использует значение из session_state
    selected = st.sidebar.multiselect(
        label, 
        opts, 
        key=key
    )
    
    # Если ничего не выбрано или выбрано "Все", возвращаем все опции
    if not selected or all_label in selected:
        return list(options)
    return selected

st.sidebar.markdown('<h2 align="center">Фильтры</h2>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

# ---------------------------------------------
# ФИЛЬТРАЦИЯ С ОПТИМИЗАЦИЕЙ
# ---------------------------------------------

if "df_filtered" not in st.session_state:
    st.session_state.df_filtered = df_clean.copy()

if "filters_applied" not in st.session_state:
    st.session_state.filters_applied = False

if "data_changed" not in st.session_state:
    st.session_state.data_changed = True



st.sidebar.markdown('<h3 align="center">Диапазон дат</h3>', unsafe_allow_html=True)
st.sidebar.caption('Выберите интервал дат для отображения.')
# Виджеты дат.
# ВАЖНО: не изменяем st.session_state['date_from_input'] / ['date_to_input'] вручную,
# чтобы избежать конфликтов между default и Session State API.
date_from = st.sidebar.date_input(
    "Дата от",
    value=df_clean['InvoiceDate'].min().date(),
    key="date_from_input"
)
date_to = st.sidebar.date_input(
    "Дата до",
    value=df_clean['InvoiceDate'].max().date(),
    key="date_to_input"
)

st.sidebar.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
st.sidebar.markdown('<h3 align="center">Мультивыбор</h3>', unsafe_allow_html=True)
st.sidebar.caption('Выберите Страны, Клиентов, Товары для отображения.')

countries = sorted(df_clean['Country'].unique())
selected_countries = multiselect_with_all("Страна", countries, key="filter_countries")

customer_ids = sorted(df_clean['CustomerID_filled'].unique())
selected_customers = multiselect_with_all("ID клиента", customer_ids, key="filter_customers")

stockcodes = sorted(df_clean['StockCode'].dropna().unique())
selected_stockcodes = multiselect_with_all("Код товара", stockcodes, key="filter_stockcodes")

descriptions = sorted(df_clean['Description'].dropna().unique())
selected_descriptions = multiselect_with_all("Товар", descriptions, key="filter_descriptions")

st.sidebar.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

butcol1, butcol2 = st.sidebar.columns(2)

# Кнопка применения фильтров
with butcol1:
    apply_filters = st.button("Применить", width='stretch')

# Применение фильтров
if apply_filters:
    st.session_state.filters_applied = True
    
    df_temp = df_clean[
        (df_clean['InvoiceDate'] >= pd.to_datetime(date_from)) &
        (df_clean['InvoiceDate'] <= pd.to_datetime(date_to)) &
        (df_clean['Country'].isin(selected_countries)) &
        (df_clean['CustomerID_filled'].isin(selected_customers)) &
        (df_clean['StockCode'].isin(selected_stockcodes)) &
        (df_clean['Description'].isin(selected_descriptions))
    ]
    if df_temp.empty:
        st.toast('Нет данных!', icon="⚠️")
    else:
        st.session_state.df_filtered = df_temp
        st.session_state.data_changed = True
        st.toast(f'Найдено {len(df_temp):,} записей', icon="✅")

with butcol2:
# Кнопка сброса (обрабатывается ДО создания виджетов)
    reset_filters = st.button("Сбросить", width='stretch')

# Обработка сброса фильтров
if reset_filters:
    # Удаляем ключи фильтров, чтобы виджеты пересоздались с "Все"
    for key in ["filter_countries", "filter_customers", "filter_stockcodes", "filter_descriptions"]:
        if key in st.session_state:
            del st.session_state[key]
    
    # Удаляем ключи дат, чтобы виджеты пересоздались с исходными значениями
    if "date_from_input" in st.session_state:
        del st.session_state.date_from_input
    if "date_to_input" in st.session_state:
        del st.session_state.date_to_input
    
    # Сбрасываем данные
    st.session_state.df_filtered = df_clean.copy()
    st.session_state.filters_applied = False
    st.session_state.data_changed = True
    
    st.toast('Фильтры сброшены', icon="🔄")
    st.rerun()

df_filtered = st.session_state.df_filtered



# ---------------------------------------------
# МЕТРИКИ С КЭШИРОВАНИЕМ
# ---------------------------------------------

def kpi_card(label, value):
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label"><h6>{label}</h6></div>
            <div class="kpi-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def format_number(value):
    return f"{value:,.0f}".replace(",", " ")

def calculate_metrics(df_filtered):
    """Пересчитывает метрики. Вызывается только при изменении данных."""
    df_sales = df_filtered[~df_filtered['IsCancelled']].copy()
    df_sales['Revenue'] = df_sales['Quantity'] * df_sales['UnitPrice']
    
    df_returns = df_filtered[df_filtered['IsCancelled'] | (df_filtered['OriginalQuantity'] < 0)].copy()
    df_returns['ReturnValue'] = abs(df_returns['OriginalQuantity'] * df_returns['UnitPrice'])
    
    metrics = {
        'total_revenue': df_sales['Revenue'].sum(),
        'total_sales': len(df_sales),
        'avg_check': df_sales.groupby('PureInvoiceNo')['Revenue'].sum().mean(),
        'unique_customers': df_sales[df_sales['CustomerID'].notna()]['CustomerID'].nunique(),
        'returns_value': df_returns['ReturnValue'].sum(),
        'df_sales': df_sales,
        'df_returns': df_returns
    }
    return metrics

# Инициализация метрик (при первом запуске)
if "metrics" not in st.session_state:
    st.session_state.metrics = calculate_metrics(df_filtered)

# Пересчитываем метрики только при изменении данных
if st.session_state.data_changed:
    st.session_state.metrics = calculate_metrics(df_filtered)

metrics = st.session_state.metrics

# Отображение метрик
st.markdown("---")
st.header("Ключевые метрики")
st.caption("Быстрый чек: выручка, средний чек, активные клиенты, возвраты. Сверяйте после изменения фильтров.")
col1, col2, col3, col4, col5 = st.columns(5)
with col1: kpi_card("Общее кол-во продаж", f"{format_number(metrics['total_sales'])}")
with col2: kpi_card("Выручка", f"£ {format_number(round(metrics['total_revenue']))}")
with col3: kpi_card("Средний чек", f"£ {format_number(round(metrics['avg_check']))}")
with col4: kpi_card("Уникальные клиенты", f"{format_number(metrics['unique_customers'])}")
with col5: kpi_card("Возвраты", f"£ {format_number(round(metrics['returns_value']))}")
st.markdown("---")

# ---------------------------------------------
# ГРАФИКИ С КЭШИРОВАНИЕМ
# ---------------------------------------------

st.header("Графики и визуализация")

pio.templates["custom_dark"] = pio.templates["plotly_dark"]
pio.templates["custom_dark"].layout.update(
    {
        "paper_bgcolor": "#0D1117",
        "plot_bgcolor": "#0D1117",
        "font": {"color": "#E6E6E6"},
        "colorway": ["#4B88FF", "#5E9CFF", "#7BB1FF", "#98C6FF", "#B5DAFF"]
    }
)
pio.templates.default = "custom_dark"

def show_plot(fig, x="", y=""):
    fig.update_layout(
        paper_bgcolor="#161B22",
        plot_bgcolor='#161B22',
        xaxis_title=x,
        yaxis_title=y
    )   
    # Конфигурацию Plotly передаем через config; используем только поддерживаемые аргументы
    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displaylogo": False, "responsive": True}
    )

def create_all_charts(df_sales, df_returns):
    """Создаёт все графики."""
    charts = {}
    
    df_product = (df_sales.groupby('Description')['Revenue']
                  .sum()
                  .sort_values(ascending=False)
                  .head(20)
                  .reset_index())
    charts['top_products'] = px.bar(df_product, x='Revenue', y='Description', 
                                    orientation='h', title="     Топ товаров по выручке")
    
    df_activity = (df_sales.groupby('CustomerID')['PureInvoiceNo']
                   .nunique()
                   .reset_index())
    df_activity.columns = ['CustomerID', 'Transactions']
    charts['activity'] = px.histogram(df_activity, x='Transactions', nbins=30,
                                      title="     Активность клиентов")
    
    df_daily = (df_sales.groupby(df_sales['InvoiceDate'].dt.date)['Revenue']
                .sum()
                .reset_index())
    charts['daily_revenue'] = px.line(df_daily, x='InvoiceDate', y='Revenue', 
                                      title="     Выручка по дням")
    
    df_country_all = (df_sales.groupby('Country')
                      .apply(lambda x: (x['Quantity'] * x['UnitPrice']).sum())
                      .reset_index(name='Revenue'))
    
    charts['country_all'] = px.bar(df_country_all.sort_values('Revenue', ascending=False),
                                   x='Country', y='Revenue', title="     Выручка по странам")
    
    df_country_no_uk = df_country_all[df_country_all['Country'] != 'United Kingdom']
    charts['country_no_uk'] = px.bar(df_country_no_uk.sort_values('Revenue', ascending=False),
                                     x='Country', y='Revenue', title="     Выручка по странам (без UK)")
    
    df_top_country_all = df_country_all.nlargest(10, 'Revenue')
    charts['top_country_all'] = px.bar(df_top_country_all.sort_values('Revenue'),
                                       x='Revenue', y='Country', orientation='h',
                                       title="     ТОП стран по выручке")
    
    df_top_country_no_uk = df_country_no_uk.nlargest(10, 'Revenue')
    charts['top_country_no_uk'] = px.bar(df_top_country_no_uk.sort_values('Revenue'),
                                         x='Revenue', y='Country', orientation='h',
                                         title="     ТОП стран по выручке (без UK)")
    
    df_ret_daily = (df_returns.groupby(df_returns['InvoiceDate'].dt.date)['ReturnValue']
                    .sum()
                    .reset_index())
    charts['returns_daily'] = px.line(df_ret_daily, x='InvoiceDate', y='ReturnValue',
                                      title="     Возвраты по времени")
    
    df_ret_prod = (df_returns.groupby('Description')['ReturnValue']
                   .sum()
                   .sort_values(ascending=False)
                   .head(20)
                   .reset_index())
    charts['returns_products'] = px.bar(df_ret_prod, x='ReturnValue', y='Description', 
                                        orientation='h', title="     ТОП товаров по возвратам")
    
    return charts

# Инициализация графиков (при первом запуске)
if "charts" not in st.session_state:
    with st.spinner("Первая загрузка графиков..."):
        st.session_state.charts = create_all_charts(
            metrics['df_sales'],
            metrics['df_returns']
        )

# Строим графики только при изменении данных
if st.session_state.data_changed:
    with st.spinner("Строим графики..."):
        st.session_state.charts = create_all_charts(
            metrics['df_sales'],
            metrics['df_returns']
        )
        st.session_state.data_changed = False

charts = st.session_state.charts

# Отображение графиков
tab1, tab2, tab3 = st.tabs(["Продажи и активность","Страны", "Возвраты"])

with tab1:
    st.caption("Смотрите лидеров по товарам и активность клиентов; падения на линии — провалы в продажах.")
    g1, g2 = st.columns([1, 2])
    with g1:
        show_plot(charts['top_products'], x="Выручка", y="Товар")
    with g2:
        show_plot(charts['activity'], x="Транзакции", y="Кол-во")
    show_plot(charts['daily_revenue'], x="Дата", y="Прибыль")

with tab2:
    st.caption("ТОП-страны — куда усиливать маркетинг; низ списка — зоны роста.")
    g_coun1, g_coun2 = st.columns(2)
    with g_coun1:
        show_plot(charts['country_all'], x="Страна", y="Выручка")
    with g_coun2:
        show_plot(charts['country_no_uk'], x="Страна", y="Выручка")
    g_coun3, g_coun4 = st.columns(2)
    with g_coun3:
        show_plot(charts['top_country_all'], x="Выручка", y="Страна")
    with g_coun4:
        show_plot(charts['top_country_no_uk'], x="Выручка", y="Страна")

with tab3:
    st.caption("Пики возвратов — ищите причины (качество, описание, логистика); проблемные товары в списке справа.")
    g_ret1, g_ret2 = st.columns(2)
    with g_ret1:
        show_plot(charts['returns_daily'], x="Дата", y="Кол-во возвратов")
    with g_ret2:
        show_plot(charts['returns_products'], x="Кол-во возвратов", y="Товар")

# ---------------------------------------------
# Таблица данных с пагинацией
# ---------------------------------------------
st.markdown("---")
st.header("Отфильтрованная таблица")

st.dataframe(df_filtered, width='stretch')

@st.cache_data(show_spinner=False)
def prepare_csv(df_filtered):
    return df_filtered.to_csv(index=False).encode("utf-8")

csv_data = prepare_csv(df_filtered)

e1, e2, e3, e4, but = st.columns([2, 2, 2, 2, 1])
with but:
    st.download_button(
        label="Скачать CSV",
        data=csv_data,
        file_name="filtered_data.csv",
        mime="text/csv",
        width='stretch'
    )

st.markdown("---")
st.markdown("""
    <div class="landing-footer">
        <p>Разработано как демонстрационный проект для портфолио</p>
        <p>Готов создать аналогичное решение для вашего бизнеса</p>
        <p><b>Telegram:</b><br>
            <a href='https://t.me/pompeedu' target='_blank'>
                @pompeedu
            </a>
        </p>
        <p><b>Email:</b><br>
            <a href='mailto:firuzjonkurbonov735700@gmail.com' target='_blank'>
                firuzjonkurbonov735700@gmail.com
            </a>
        </p>
    </div>
    """, unsafe_allow_html=True)
