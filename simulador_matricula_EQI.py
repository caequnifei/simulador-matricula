from datetime import date
import html

import streamlit as st


# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Fluxograma Inteligente - Engenharia Química UNIFEI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# ESTILO - SOMENTE MODO CLARO
# ============================================================

st.markdown(
    """
<style>
:root {
    --caemt-color: #14532D;
    --unifei-color: #0056B3;
    --background-color: #FFFFFF;
    --secondary-background: #F7F9FC;
    --text-color: #1F2937;
    --muted-color: #5F6B7A;
    --border-color: #D8DEE8;

    --suggestion-bg: #EAF7EE;
    --suggestion-border: #18864B;
    --suggestion-text: #126836;

    --blocked-bg: #FDECEC;
    --blocked-border: #C93434;
    --blocked-text: #A32121;

    --neutral-bg: #F7F9FC;
    --neutral-border: #D8DEE8;
    --neutral-text: #475467;
}

html,
body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    color-scheme: light !important;
}

[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"] {
    background-color: var(--background-color) !important;
    color: var(--text-color) !important;
}

[data-testid="stHeader"] {
    background-color: rgba(255, 255, 255, 0.96) !important;
}

#MainMenu,
footer {
    visibility: hidden;
}


/* ==========================================================
   CORREÇÃO MÍNIMA DOS WIDGETS NATIVOS DO STREAMLIT
   Mantém toda a lógica e as duas grades inalteradas.
   ========================================================== */

/* Reforça as variáveis de tema usadas pelo Streamlit. */
:root,
[data-testid="stAppViewContainer"] {
    --st-primary-color: #4A148C !important;
    --st-background-color: #FFFFFF !important;
    --st-secondary-background-color: #F7F9FC !important;
    --st-text-color: #1F2937 !important;
    color-scheme: light !important;
}

/* SELECTBOX: caixa fechada */
/* Compatibilidade com versões novas do Streamlit: o campo visível pode
   ser renderizado como combobox sem o antigo data-baseweb="select". */
[data-testid="stSelectbox"] [role="combobox"],
[data-testid="stSelectbox"] div:has(> [role="combobox"]),
[data-testid="stSelectbox"] div[data-baseweb="select"],
[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background: #FFFFFF !important;
    background-color: #FFFFFF !important;
    color: #1F2937 !important;
    border-color: #D8DEE8 !important;
    box-shadow: none !important;
}

[data-testid="stSelectbox"] [role="combobox"] * {
    color: #1F2937 !important;
}

[data-testid="stSelectbox"] [role="combobox"] svg,
[data-testid="stSelectbox"] div:has(> [role="combobox"]) svg {
    color: #1F2937 !important;
    fill: #1F2937 !important;
}

[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    color: #1F2937 !important;
    border: 1px solid #D8DEE8 !important;
    box-shadow: none !important;
}

[data-testid="stSelectbox"] div[data-baseweb="select"] > div:hover,
[data-testid="stSelectbox"] div[data-baseweb="select"] > div:focus-within {
    background-color: #FFFFFF !important;
    border-color: #98A2B3 !important;
}

[data-testid="stSelectbox"] div[data-baseweb="select"] span,
[data-testid="stSelectbox"] div[data-baseweb="select"] div,
[data-testid="stSelectbox"] div[data-baseweb="select"] p {
    color: #1F2937 !important;
}

[data-testid="stSelectbox"] div[data-baseweb="select"] svg {
    color: #1F2937 !important;
    fill: #1F2937 !important;
}

/* SELECTBOX: menu aberto */
div[data-baseweb="popover"],
div[data-baseweb="menu"],
ul[role="listbox"] {
    background-color: #FFFFFF !important;
    color: #1F2937 !important;
}

li[role="option"] {
    background-color: #FFFFFF !important;
    color: #1F2937 !important;
}

li[role="option"]:hover,
li[role="option"][aria-selected="true"] {
    background-color: #F1F4F8 !important;
    color: #1F2937 !important;
}

/* BOTÕES */
[data-testid="stButton"] button {
    background-color: #FFFFFF !important;
    color: #1F2937 !important;
    border: 1px solid #D8DEE8 !important;
    box-shadow: none !important;
}

[data-testid="stButton"] button:hover {
    background-color: #F7F9FC !important;
    color: #4A148C !important;
    border-color: #4A148C !important;
}

[data-testid="stButton"] button:disabled {
    background-color: #F7F9FC !important;
    color: #98A2B3 !important;
    border-color: #D8DEE8 !important;
    opacity: 1 !important;
}

/* CHECKBOXES - Streamlit atual (React Aria).
   O indicador visual fica dentro do label. Pode existir um input oculto antes dele,
   por isso usamos div:first-of-type em vez de div:first-child. */
[data-testid="stCheckbox"] label > div:first-of-type {
    background-color: #FFFFFF !important;
    background: #FFFFFF !important;
    border: 1px solid #98A2B3 !important;
    box-shadow: none !important;
}

/* Mantém o fundo branco quando o checkbox está marcado. */
[data-testid="stCheckbox"] label[data-selected] > div:first-of-type,
[data-testid="stCheckbox"] label:has(input[type="checkbox"]:checked) > div:first-of-type {
    background-color: #FFFFFF !important;
    background: #FFFFFF !important;
    border-color: #14532D !important;
}

/* Tique verde escuro. */
[data-testid="stCheckbox"] label[data-selected] > div:first-of-type svg,
[data-testid="stCheckbox"] label:has(input[type="checkbox"]:checked) > div:first-of-type svg {
    stroke: #14532D !important;
    color: #14532D !important;
    fill: none !important;
}

/* Fallback para versões anteriores do Streamlit/BaseWeb. */
[data-testid="stCheckbox"] [role="checkbox"],
[data-testid="stCheckbox"] label[data-baseweb="checkbox"] > span:first-child,
[data-testid="stCheckbox"] label[data-baseweb="checkbox"] > div:first-child {
    background-color: #FFFFFF !important;
    background: #FFFFFF !important;
    border-color: #98A2B3 !important;
}

[data-testid="stCheckbox"] input[type="checkbox"] {
    accent-color: #14532D !important;
    color-scheme: light !important;
}

[data-testid="stCheckbox"] label,
[data-testid="stCheckbox"] label span,
[data-testid="stCheckbox"] label p {
    color: #1F2937 !important;
}

/* Campos BaseWeb genéricos, caso o Streamlit altere a implementação interna. */
[data-baseweb="input"] > div,
[data-baseweb="textarea"] > div {
    background-color: #FFFFFF !important;
    color: #1F2937 !important;
    border-color: #D8DEE8 !important;
}

input,
textarea {
    color-scheme: light !important;
}

.brand-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 1.05rem;
    font-weight: 800;
    margin-bottom: -8px;
}

.brand-caemt {
    color: var(--caemt-color) !important;
}

.brand-unifei {
    color: var(--unifei-color) !important;
}

h1 {
    text-align: center;
    color: var(--text-color) !important;
    font-weight: 800;
    margin-top: 10px;
}

h2,
h3 {
    color: var(--text-color) !important;
}

.subtitle {
    text-align: center;
    color: var(--muted-color) !important;
    margin-top: -8px;
    margin-bottom: 22px;
}

.semester-badge-container {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    width: 100%;
    padding-top: 29px;
}

.semester-badge {
    width: fit-content;
    margin: 0;
    padding: 7px 12px;
    border-radius: 999px;
    background: #EEF4FF;
    border: 1px solid #C9DBF5;
    color: var(--unifei-color) !important;
    font-size: 0.84rem;
    font-weight: 700;
    white-space: nowrap;
}

[data-testid="stWidgetLabel"] p,
[data-testid="stCheckbox"] p {
    color: var(--text-color) !important;
}

[data-testid="stExpander"] {
    background-color: #FFFFFF !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 9px !important;
    overflow: hidden;
}

[data-testid="stExpander"] summary {
    background-color: var(--secondary-background) !important;
}

[data-testid="stExpander"] summary:hover {
    background-color: #EEF2F7 !important;
}

[data-testid="stExpander"] summary p {
    color: var(--text-color) !important;
    font-weight: 700;
}

hr {
    border-color: var(--border-color) !important;
    opacity: 0.8;
}

.status-bar {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 28px;
    padding: 18px 24px;
    margin: 22px 0 26px 0;
    background: var(--secondary-background);
    border: 1px solid var(--border-color);
    border-radius: 10px;
}

.status-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 5px;
    min-width: 125px;
}

.status-label {
    color: var(--muted-color) !important;
    font-size: 0.70rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    text-align: center;
}

.status-value {
    color: var(--unifei-color) !important;
    font-size: 1.72rem;
    font-weight: 800;
    line-height: 1;
}

.status-divider {
    width: 1px;
    height: 42px;
    background-color: var(--border-color);
}

.sugestao-item,
.bloqueada-oferta,
.bloqueada-requisito {
    padding: 12px 15px;
    margin-bottom: 9px;
    border-radius: 7px;
    font-size: 0.94rem;
    line-height: 1.45;
}

.sugestao-item {
    background-color: var(--suggestion-bg);
    border: 1px solid #CAE9D5;
    border-left: 4px solid var(--suggestion-border);
    color: var(--suggestion-text) !important;
}

.sugestao-item strong {
    color: var(--suggestion-text) !important;
}

.bloqueada-oferta {
    background-color: var(--blocked-bg);
    border: 1px solid #F4CDCD;
    border-left: 4px solid var(--blocked-border);
    color: var(--blocked-text) !important;
}

.bloqueada-oferta strong,
.bloqueada-oferta span {
    color: var(--blocked-text) !important;
}

.bloqueada-requisito {
    background-color: var(--neutral-bg);
    border: 1px solid var(--neutral-border);
    border-left: 4px solid #98A2B3;
    color: var(--neutral-text) !important;
}

.bloqueada-requisito strong,
.bloqueada-requisito span {
    color: var(--neutral-text) !important;
}

.aviso-oferta,
.aviso-requisito {
    display: block;
    margin-top: 4px;
    font-size: 0.80rem;
    font-weight: 600;
}

.divisoria {
    margin: 24px 0 13px 0;
    padding-bottom: 7px;
    border-bottom: 1px solid var(--border-color);
    color: var(--muted-color) !important;
    font-size: 0.76rem;
    font-weight: 800;
    letter-spacing: 0.35px;
}

.small-note {
    color: var(--muted-color) !important;
    font-size: 0.82rem;
}

@media (max-width: 768px) {
    .brand-container {
        font-size: 0.92rem;
    }

    h1 {
        font-size: 1.9rem !important;
    }

    .subtitle {
        font-size: 0.91rem;
    }

    .status-bar {
        gap: 8px;
        padding: 14px 6px;
    }

    .status-item {
        min-width: 0;
        flex: 1;
    }

    .status-label {
        font-size: 0.57rem;
    }

    .status-value {
        font-size: 1.30rem;
    }

    .status-divider {
        height: 34px;
    }

    .semester-badge-container {
        justify-content: flex-start;
        padding-top: 0;
        margin-bottom: 10px;
    }

    .semester-badge {
        white-space: normal;
    }
}
</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# MATRIZES CURRICULARES
# ============================================================
#
# "oferta":
#   impar   -> 1º semestre do ano
#   par     -> 2º semestre do ano
#   regular -> pode ser ofertada nos dois semestres
#
# "req" contém os componentes que precisam estar concluídos
# para a disciplina aparecer como liberada no simulador.
# ============================================================

# Grade nova de Engenharia Química (arquivo de referência com componentes 2023).
#
# IMPORTANTE:
# O simulador original registra apenas disciplinas CONCLUÍDAS. Por isso, o campo
# "req" abaixo representa somente PRÉ-REQUISITOS TOTAIS que podem ser verificados
# a partir dessa informação. Pré-requisitos parciais e co-requisitos continuam
# sujeitos à conferência no SIGAA, conforme o aviso já existente no rodapé.
#
# Os arquivos fornecidos não informam a periodicidade real de oferta das turmas.
# Para não criar restrições que não constam nas fontes, "oferta" foi mantida como
# "regular" em todos os componentes de EQI.
MATRIZ_2023 = {
    "1º Período": {
        "EQI100": {"nome": "Introdução à Engenharia Química", "req": [], "oferta": "regular"},
        "IEPG21": {"nome": "Ciências Humanas e Sociais", "req": [], "oferta": "regular"},
        "LET013": {"nome": "Escrita Acadêmico Científica", "req": [], "oferta": "regular"},
        "MAT00A": {"nome": "Cálculo A", "req": [], "oferta": "regular"},
        "QUI016": {"nome": "Química Geral", "req": [], "oferta": "regular"},
        "QUI017": {"nome": "Química Geral Experimental", "req": [], "oferta": "regular"},
    },
    "2º Período": {
        "DES005": {"nome": "Desenho Técnico Básico", "req": [], "oferta": "regular"},
        "EQI101": {"nome": "Fundamentos da Engenharia Química I", "req": ["EQI100"], "oferta": "regular"},
        "FIS210": {"nome": "Física I", "req": [], "oferta": "regular"},
        "FIS212": {"nome": "Física Experimental I", "req": [], "oferta": "regular"},
        "MAT00B": {"nome": "Cálculo B", "req": ["MAT00A"], "oferta": "regular"},
        "MAT00D": {"nome": "Equações Diferenciais A", "req": ["MAT00A"], "oferta": "regular"},
        "QUI023": {"nome": "Química Inorgânica", "req": ["QUI016"], "oferta": "regular"},
    },
    "3º Período": {
        "EQI102": {"nome": "Processos Químicos Industriais", "req": ["EQI100"], "oferta": "regular"},
        "EQI103": {"nome": "Fundamentos da Engenharia Química II", "req": ["EQI101"], "oferta": "regular"},
        "EQI104": {"nome": "Fundamentos de Programação", "req": ["EQI100"], "oferta": "regular"},
        "MAT00C": {"nome": "Cálculo C", "req": ["MAT00B"], "oferta": "regular"},
        "MAT00N": {"nome": "Cálculo Numérico", "req": ["MAT00A"], "oferta": "regular"},
        "QUI022": {"nome": "Química Orgânica", "req": ["QUI016"], "oferta": "regular"},
        "QUI068": {"nome": "Química Orgânica Experimental I", "req": [], "oferta": "regular"},
    },
    "4º Período": {
        "EQI105": {"nome": "Termodinâmica para Engenharia Química I", "req": ["EQI103", "MAT00B"], "oferta": "regular"},
        "EQI106": {"nome": "Ferramentas Computacionais na Engenharia Química", "req": ["EQI104"], "oferta": "regular"},
        "FIS410": {"nome": "Física III", "req": ["FIS210"], "oferta": "regular"},
        "IRN005": {"nome": "Estatística para Ciências Ambientais e Engenharia", "req": [], "oferta": "regular"},
        "MAT00E": {"nome": "Equações Diferenciais B", "req": ["MAT00D"], "oferta": "regular"},
        "QUI105": {"nome": "Química Analítica", "req": ["QUI016"], "oferta": "regular"},
        "QUI115": {"nome": "Química Analítica Experimental", "req": ["QUI016"], "oferta": "regular"},
    },
    "5º Período": {
        "EBP020": {"nome": "Bioquímica e Microbiologia", "req": [], "oferta": "regular"},
        "EEB100": {"nome": "Eletricidade Básica I", "req": [], "oferta": "regular"},
        "EME303": {"nome": "Mecânica Vetorial Estática", "req": [], "oferta": "regular"},
        "EQI004": {"nome": "Fenômenos de Transporte I", "req": [], "oferta": "regular"},
        "EQI107": {"nome": "Termodinâmica para Engenharia Química II", "req": ["EQI105"], "oferta": "regular"},
        "EQI108": {"nome": "Fundamentos de Instrumentação para Engenharia Química", "req": ["EQI004"], "oferta": "regular"},
        "EQI109P": {"nome": "Cinética Química Aplicada Experimental", "req": [], "oferta": "regular"},
        "EQI109T": {"nome": "Cinética Química Aplicada", "req": ["QUI016", "EQI103"], "oferta": "regular"},
    },
    "6º Período": {
        "EQI012": {"nome": "Laboratório de Engenharia Química I", "req": ["EQI105", "EQI100"], "oferta": "regular"},
        "EQI013": {"nome": "Fenômenos de Transporte II", "req": ["EQI004"], "oferta": "regular"},
        "EQI110": {"nome": "Materiais para Indústria Química", "req": ["EQI100"], "oferta": "regular"},
        "EQI111P": {"nome": "Projeto de Reatores Químicos I - Experimental", "req": [], "oferta": "regular"},
        "EQI111T": {"nome": "Projeto de Reatores Químicos I", "req": ["EQI109T"], "oferta": "regular"},
        "EQI112": {"nome": "Modelagem e Simulação de Processos Químicos", "req": ["MAT00N"], "oferta": "regular"},
        "EQI113": {"nome": "Operações Unitárias da Indústria Química I", "req": [], "oferta": "regular"},
    },
    "7º Período": {
        "EBP012": {"nome": "Engenharia Bioquímica", "req": [], "oferta": "regular"},
        "EQI021": {"nome": "Laboratório de Engenharia Química II", "req": ["EQI012"], "oferta": "regular"},
        "EQI022": {"nome": "Fenômenos de Transporte III", "req": ["EQI013"], "oferta": "regular"},
        "EQI114P": {"nome": "Projeto de Reatores Químicos II - Experimental", "req": [], "oferta": "regular"},
        "EQI114T": {"nome": "Projeto de Reatores Químicos II", "req": ["EQI111T"], "oferta": "regular"},
        "EQI115": {"nome": "Operações Unitárias da Indústria Química II", "req": [], "oferta": "regular"},
        "EQI116": {"nome": "Controle de Processos Químicos", "req": ["EQI112"], "oferta": "regular"},
    },
    "8º Período": {
        "EQI024": {"nome": "Desenvolvimento de Processos Químicos", "req": ["EQI100", "EQI110", "EQI115"], "oferta": "regular"},
        "EQI029": {"nome": "Laboratório de Engenharia Química III", "req": ["EQI021"], "oferta": "regular"},
        "EQI054": {"nome": "Instalações na Indústria Química", "req": [], "oferta": "regular"},
        "EQI117": {"nome": "Tecnologia e Aplicação dos Materiais", "req": ["EQI110"], "oferta": "regular"},
        "EQI118": {"nome": "Operações Unitárias da Indústria Química III", "req": [], "oferta": "regular"},
        "EQI119": {"nome": "Otimização de Processos Químicos", "req": ["EQI112"], "oferta": "regular"},
        "IEPG10": {"nome": "Engenharia Econômica", "req": [], "oferta": "regular"},
    },
    "9º Período": {
        "EQI120": {"nome": "Controle Ambiental e Tratamento de Resíduos na Indústria Química", "req": ["EQI113"], "oferta": "regular"},
        "EQI121": {"nome": "Síntese e Simuladores de Processos Químicos", "req": ["EQI112"], "oferta": "regular"},
        "IEPG22": {"nome": "Administração Aplicada", "req": [], "oferta": "regular"},
        "TCC1EQI2023": {"nome": "Trabalho de Conclusão de Curso I", "req": [], "oferta": "regular"},
    },
    "10º Período": {
        "ESTEQI2023": {"nome": "Estágio Supervisionado", "req": [], "oferta": "regular"},
        "TCC2EQI2023": {"nome": "Trabalho de Conclusão de Curso II", "req": [], "oferta": "regular"},
    },
}


# Grade antiga de Engenharia Química, transcrita do fluxo curricular enviado.
# Alguns códigos escritos como "EQUI" no arquivo foram normalizados para "EQI"
# para manter consistência entre a disciplina e seus pré-requisitos.
MATRIZ_2016 = {
    "1º Período": {
        "MAT001": {"nome": "Cálculo I", "req": [], "oferta": "regular"},
        "MAT011": {"nome": "Geometria Analítica e Álgebra Linear", "req": [], "oferta": "regular"},
        "FIS104": {"nome": "Metodologia Científica", "req": [], "oferta": "regular"},
        "FIS114": {"nome": "Laboratório de Metodologia Científica", "req": [], "oferta": "regular"},
        "QUI016": {"nome": "Química Geral", "req": [], "oferta": "regular"},
        "QUI017": {"nome": "Química Geral Experimental", "req": [], "oferta": "regular"},
        "EQI001": {"nome": "Introdução a Engenharia Química", "req": [], "oferta": "regular"},
    },
    "2º Período": {
        "MAT002": {"nome": "Cálculo II", "req": ["MAT001", "MAT011"], "oferta": "regular"},
        "MAT013": {"nome": "Probabilidade e Estatística", "req": ["MAT001", "MAT011"], "oferta": "regular"},
        "FIS203": {"nome": "Física I", "req": [], "oferta": "regular"},
        "FIS213": {"nome": "Física Experimental I", "req": [], "oferta": "regular"},
        "QUI023": {"nome": "Química Inorgânica", "req": ["QUI016"], "oferta": "regular"},
        "DES201": {"nome": "Desenho Técnico Básico", "req": [], "oferta": "regular"},
        "BAC002": {"nome": "Comunicação e Expressão", "req": [], "oferta": "regular"},
    },
    "3º Período": {
        "MAT003": {"nome": "Cálculo III", "req": ["MAT001", "MAT011"], "oferta": "regular"},
        "MAT021": {"nome": "Equações Diferenciais I", "req": ["MAT001", "MAT011"], "oferta": "regular"},
        "SOC002": {"nome": "Ciências Humanas e Sociais", "req": [], "oferta": "regular"},
        "QUI022": {"nome": "Química Orgânica", "req": ["QUI016"], "oferta": "regular"},
        "QUI068": {"nome": "Química Orgânica Experimental", "req": ["QUI016"], "oferta": "regular"},
        "CCO016": {"nome": "Fundamentos de Programação", "req": [], "oferta": "regular"},
        "EQI002": {"nome": "Balanço de Massa e Energia", "req": [], "oferta": "regular"},
    },
    "4º Período": {
        "MAT012": {"nome": "Cálculo Numérico", "req": ["MAT001"], "oferta": "regular"},
        "MAT022": {"nome": "Equações Diferenciais II", "req": ["MAT001", "MAT021"], "oferta": "regular"},
        "FIS403": {"nome": "Física III", "req": ["MAT001"], "oferta": "regular"},
        "QUI105": {"nome": "Química Analítica", "req": ["QUI016"], "oferta": "regular"},
        "QUI115": {"nome": "Química Analítica Experimental", "req": ["QUI016"], "oferta": "regular"},
        "EQI005": {"nome": "Termodinâmica Química I", "req": [], "oferta": "regular"},
        "EAM002": {"nome": "Ciências do Meio Ambiente", "req": [], "oferta": "regular"},
    },
    "5º Período": {
        "EQI004": {"nome": "Fenômenos de Transporte I", "req": [], "oferta": "regular"},
        "EQI008": {"nome": "Processos Químicos Industriais", "req": [], "oferta": "regular"},
        "EBP020": {"nome": "Bioquímica e Microbiologia", "req": [], "oferta": "regular"},
        "EEL310": {"nome": "Eletricidade I", "req": [], "oferta": "regular"},
        "EQI007": {"nome": "Termodinâmica Química II", "req": ["EQI005"], "oferta": "regular"},
        "ECN001": {"nome": "Economia", "req": [], "oferta": "regular"},
        "EME311": {"nome": "Mecânica dos Sólidos", "req": [], "oferta": "regular"},
    },
    "6º Período": {
        "EQI013": {"nome": "Fenômenos de Transporte II", "req": ["EQI004"], "oferta": "regular"},
        "EQI011": {"nome": "Operações Unitárias I", "req": [], "oferta": "regular"},
        "EQI009": {"nome": "Instrumentação na Indústria Química", "req": [], "oferta": "regular"},
        "EQI012": {"nome": "Laboratório de Engenharia Química I", "req": [], "oferta": "regular"},
        "EQI003": {"nome": "Cinética Química e Reatores Químicos", "req": ["EQI002"], "oferta": "regular"},
        "EQI006": {"nome": "Materiais para a Indústria Química", "req": [], "oferta": "regular"},
        "EPR502": {"nome": "Engenharia Econômica", "req": [], "oferta": "regular"},
    },
    "7º Período": {
        "EQI022": {"nome": "Fenômenos de Transporte III", "req": ["EQI013"], "oferta": "regular"},
        "EQI019": {"nome": "Operações Unitárias II", "req": [], "oferta": "regular"},
        "EQI010": {"nome": "Modelagem e Simulação de Processos Químicos I", "req": ["MAT012"], "oferta": "regular"},
        "EQI021": {"nome": "Laboratório de Engenharia Química II", "req": [], "oferta": "regular"},
        "EBP012": {"nome": "Engenharia Bioquímica", "req": [], "oferta": "regular"},
        "EQI023": {"nome": "Projeto de Reatores Químicos", "req": [], "oferta": "regular"},
    },
    "8º Período": {
        "EQI024": {"nome": "Desenvolvimento de Processos Químicos", "req": ["EPR502", "EQI019"], "oferta": "regular"},
        "EQI027": {"nome": "Operações Unitárias III", "req": [], "oferta": "regular"},
        "EQI030P/EQI030T": {"nome": "Controle de Processos Químicos I", "req": [], "oferta": "regular"},
        "EQI020": {"nome": "Modelagem e Simulação de Processos Químicos II", "req": ["EQI010"], "oferta": "regular"},
        "EQI031": {"nome": "Projeto de Reatores II", "req": ["EQI022", "EQI023"], "oferta": "regular"},
        "EQI029": {"nome": "Laboratório de Engenharia Química III", "req": [], "oferta": "regular"},
    },
    "9º Período": {
        "EQI032": {"nome": "Síntese e Simuladores de Processos Químicos", "req": ["EQI024"], "oferta": "regular"},
        "EBP031": {"nome": "Tratamento de Resíduos da Indústria Química", "req": [], "oferta": "regular"},
        "EQI053.1/EQI053.2": {"nome": "Controle de Processos Químicos II", "req": [], "oferta": "regular"},
        "EQI052": {"nome": "Fundamentos de Otimização para Processos Químicos", "req": ["MAT003"], "oferta": "regular"},
        "EQI054": {"nome": "Instalações na Indústria Química", "req": [], "oferta": "regular"},
        "EPR002": {"nome": "Organização Industrial e Administração", "req": [], "oferta": "regular"},
    },
    "10º Período": {
        "TFG": {"nome": "Trabalho Final de Graduação", "req": [], "oferta": "regular"},
        "EST": {"nome": "Estágio Supervisionado", "req": [], "oferta": "regular"},
    },
}

MATRIZES = {
    "2023": MATRIZ_2023,
    "2016": MATRIZ_2016,
}


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================


def todas_as_disciplinas(matriz):
    """Retorna um dicionário código -> dados para a matriz selecionada."""
    resultado = {}
    for periodo, materias in matriz.items():
        for codigo, dados in materias.items():
            resultado[codigo] = {**dados, "periodo": periodo}
    return resultado


def proximo_semestre_referencia(hoje=None):
    """Retorna (oferta, texto) para o próximo semestre civil."""
    hoje = hoje or date.today()
    if hoje.month <= 6:
        return "par", f"2º semestre de {hoje.year}"
    return "impar", f"1º semestre de {hoje.year + 1}"


def chave_checkbox(grade, codigo):
    return f"concluida_{grade}_{codigo}"


def inicializar_estado(grade, disciplinas):
    for codigo in disciplinas:
        chave = chave_checkbox(grade, codigo)
        if chave not in st.session_state:
            st.session_state[chave] = False


def disciplinas_concluidas(grade, disciplinas):
    return {
        codigo
        for codigo in disciplinas
        if st.session_state.get(chave_checkbox(grade, codigo), False)
    }


def marcar_periodo(grade, matriz, periodo, valor):
    for codigo in matriz[periodo]:
        st.session_state[chave_checkbox(grade, codigo)] = valor


def limpar_todas(grade, disciplinas):
    for codigo in disciplinas:
        st.session_state[chave_checkbox(grade, codigo)] = False


def escapar(texto):
    return html.escape(str(texto))


def requisito_esta_concluido(grade, requisito, concluidas):
    return requisito in concluidas


def nome_requisito(grade, requisito, disciplinas):
    return requisito


def renderizar_disponivel(codigo, dados):
    st.markdown(
        '<div class="sugestao-item">'
        f'<strong>{escapar(codigo)}</strong> - {escapar(dados["nome"])}'
        '</div>',
        unsafe_allow_html=True,
    )


def renderizar_nao_ofertada(codigo, dados, semestre_destino):
    if dados["oferta"] == "impar":
        oferta_texto = "Componente previsto para o 1º semestre do ano."
    else:
        oferta_texto = "Componente previsto para o 2º semestre do ano."

    st.markdown(
        '<div class="bloqueada-oferta">'
        f'<strong>{escapar(codigo)}</strong> - {escapar(dados["nome"])}'
        f'<span class="aviso-oferta">{escapar(oferta_texto)} Destino atual: {escapar(semestre_destino)}.</span>'
        '</div>',
        unsafe_allow_html=True,
    )


def renderizar_bloqueada(codigo, dados, faltantes):
    faltantes_html = ", ".join(escapar(item) for item in faltantes)
    st.markdown(
        '<div class="bloqueada-requisito">'
        f'<strong>{escapar(codigo)}</strong> - {escapar(dados["nome"])}'
        f'<span class="aviso-requisito">Falta concluir: {faltantes_html}</span>'
        '</div>',
        unsafe_allow_html=True,
    )


# ============================================================
# CABEÇALHO
# ============================================================

st.markdown(
    '<div class="brand-container">'
    '<div class="brand-caemt">CAEQ</div>'
    '<div class="brand-unifei">UNIFEI</div>'
    '</div>',
    unsafe_allow_html=True,
)

st.markdown("<h1>Fluxograma Inteligente</h1>", unsafe_allow_html=True)

st.markdown(
    '<p class="subtitle">'
    'Escolha a matriz curricular e marque apenas as disciplinas que você já concluiu.'
    '</p>',
    unsafe_allow_html=True,
)


# ============================================================
# SELEÇÃO DA MATRIZ
# ============================================================

col_grade, col_planejamento = st.columns([1.2, 2.8])

with col_grade:
    grade_rotulo = st.selectbox(
        "Grade curricular:",
        options=["Atual", "Anterior"],
        index=0,
    )


grade_versao = {"Atual": "2023", "Anterior": "2016"}[grade_rotulo]
MATRIZ_ATUAL = MATRIZES[grade_versao]
DISCIPLINAS = todas_as_disciplinas(MATRIZ_ATUAL)
inicializar_estado(grade_versao, DISCIPLINAS)

semestre_oferta, semestre_texto = proximo_semestre_referencia()

with col_planejamento:
    st.markdown(
        '<div class="semester-badge-container">'
        f'<div class="semester-badge">Grade {escapar(grade_rotulo)} · Planejamento automático: {escapar(semestre_texto)}</div>'
        '</div>',
        unsafe_allow_html=True,
    )

# ============================================================
# CONTROLES RÁPIDOS
# ============================================================

controle1, espaco = st.columns([1, 5])

with controle1:
    if st.button(
        "Limpar seleção",
        key=f"limpar_{grade_versao}",
        use_container_width=True,
    ):
        limpar_todas(grade_versao, DISCIPLINAS)
        st.rerun()


st.markdown("---")


# ============================================================
# LAYOUT PRINCIPAL
# ============================================================

col_esquerda, col_direita = st.columns([1.18, 0.82], gap="large")


# ============================================================
# COLUNA ESQUERDA - TODAS AS DISCIPLINAS
# ============================================================

with col_esquerda:
    st.markdown("### 1. Disciplinas concluídas")
    st.caption("Abra os períodos e marque somente o que já foi concluído.")

    for periodo, materias in MATRIZ_ATUAL.items():
        concluidas_periodo = sum(
            1
            for codigo in materias
            if st.session_state.get(chave_checkbox(grade_versao, codigo), False)
        )

        titulo = f"{periodo} - {concluidas_periodo}/{len(materias)} concluídas"

        with st.expander(
            titulo,
            expanded=periodo in {"1º Período", "2º Período"},
        ):
            botao1, botao2 = st.columns(2)

            with botao1:
                if st.button(
                    "Marcar período inteiro",
                    key=f"marcar_{grade_versao}_{periodo}",
                    use_container_width=True,
                ):
                    marcar_periodo(grade_versao, MATRIZ_ATUAL, periodo, True)
                    st.rerun()

            with botao2:
                if st.button(
                    "Desmarcar período",
                    key=f"desmarcar_{grade_versao}_{periodo}",
                    use_container_width=True,
                ):
                    marcar_periodo(grade_versao, MATRIZ_ATUAL, periodo, False)
                    st.rerun()

            for codigo, dados in materias.items():
                st.checkbox(
                    f"**{codigo}** - {dados['nome']}",
                    key=chave_checkbox(grade_versao, codigo),
                )


# ============================================================
# CÁLCULOS DO ESTADO ATUAL
# ============================================================

concluidas = disciplinas_concluidas(grade_versao, DISCIPLINAS)
total_materias = len(DISCIPLINAS)
total_concluidas = len(concluidas)
progresso = round((total_concluidas / total_materias) * 100) if total_materias else 0

liberadas = []
liberadas_nao_ofertadas = []
bloqueadas = []

for codigo, dados in DISCIPLINAS.items():
    if codigo in concluidas:
        continue

    faltantes = [
        nome_requisito(grade_versao, req, DISCIPLINAS)
        for req in dados["req"]
        if not requisito_esta_concluido(grade_versao, req, concluidas)
    ]

    if faltantes:
        bloqueadas.append((codigo, dados, faltantes))
        continue

    if dados["oferta"] == "regular" or dados["oferta"] == semestre_oferta:
        liberadas.append((codigo, dados))
    else:
        liberadas_nao_ofertadas.append((codigo, dados))


# ============================================================
# BARRA DE STATUS
# ============================================================

st.markdown(
    '<div class="status-bar">'
    '<div class="status-item">'
    '<div class="status-label">Concluídas</div>'
    f'<div class="status-value">{total_concluidas}</div>'
    '</div>'
    '<div class="status-divider"></div>'
    '<div class="status-item">'
    '<div class="status-label">Total da grade</div>'
    f'<div class="status-value">{total_materias}</div>'
    '</div>'
    '<div class="status-divider"></div>'
    '<div class="status-item">'
    '<div class="status-label">Progresso</div>'
    f'<div class="status-value">{progresso}%</div>'
    '</div>'
    '</div>',
    unsafe_allow_html=True,
)


# ============================================================
# COLUNA DIREITA - RESULTADOS
# ============================================================

with col_direita:
    st.markdown("### 2. Situação para o próximo semestre")
    st.caption(f"Grade {grade_rotulo} · Análise para {semestre_texto}.")

    if liberadas:
        st.markdown(
            '<div class="divisoria">DISCIPLINAS LIBERADAS</div>',
            unsafe_allow_html=True,
        )
        for codigo, dados in liberadas:
            renderizar_disponivel(codigo, dados)
    else:
        st.info("Nenhuma disciplina foi identificada como liberada neste momento.")

    if liberadas_nao_ofertadas:
        st.markdown(
            '<div class="divisoria">LIBERADAS, MAS FORA DO SEMESTRE DE OFERTA</div>',
            unsafe_allow_html=True,
        )
        for codigo, dados in liberadas_nao_ofertadas:
            renderizar_nao_ofertada(codigo, dados, semestre_texto)

    if bloqueadas:
        with st.expander(f"Ver disciplinas ainda bloqueadas ({len(bloqueadas)})"):
            for codigo, dados, faltantes in bloqueadas:
                renderizar_bloqueada(codigo, dados, faltantes)


# ============================================================
# RODAPÉ
# ============================================================

st.markdown("---")
st.caption(
    "Ferramenta independente e não oficial. A disponibilidade real de turmas, "
    "regras acadêmicas e eventuais alterações curriculares devem ser conferidas no SIGAA/UNIFEI."
)