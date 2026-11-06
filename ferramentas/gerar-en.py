# Gera Portfolio-Rafael-Pessoa/en/index.html a partir do index.html em português.
# Ao mudar qualquer texto do site, ajuste a tabela e rode: py -3.12 ferramentas/gerar-en.py
# O script para e lista o que ficou sem tradução, para a página em inglês nunca sair pela metade.
import json, re, sys
from html.parser import HTMLParser
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
PASTA = Path(__file__).resolve().parent.parent / "Portfolio-Rafael-Pessoa"
s = (PASTA / "index.html").read_text(encoding="utf-8")

# Trechos que não são um texto inteiro: entram antes da tabela.
TRECHOS = [
    ('<html lang="pt-BR">', '<html lang="en">'),
    ('content="pt_BR"', 'content="en_US"'),
    ('<link rel="canonical" href="https://rafapessoa.com.br/">', '<link rel="canonical" href="https://rafapessoa.com.br/en/">'),
    ('<meta property="og:url" content="https://rafapessoa.com.br/">', '<meta property="og:url" content="https://rafapessoa.com.br/en/">'),
    ('"inLanguage":"pt-BR","url":"https://rafapessoa.com.br/"', '"inLanguage":"en","url":"https://rafapessoa.com.br/en/"'),
    ('<a class="nav-idioma" href="en/" hreflang="en" lang="en" aria-label="Read this page in English">EN</a>',
     '<a class="nav-idioma" href="../" hreflang="pt-BR" lang="pt-BR" aria-label="Ler esta página em português">PT</a>'),
    ('aria-label="Mudar para o modo claro"', 'aria-label="Switch to light mode"'),
    ('<span>Modelo <em>o dado</em> e</span> <span>construo o sistema</span> <span>que gera <em>o dado</em>.</span>',
     '<span>I model <em>the data</em></span> <span>and build the system</span> <span>that generates <em>it</em>.</span>'),
    ('ORDER BY periodo DESC', 'ORDER BY period DESC'),
    ("'ORDER BY ' + chave + ' '", "'ORDER BY ' + ({ empresa: 'company', periodo: 'period', funcao: 'role', stack: 'stack', resultado: 'result' })[chave] + ' '"),
    ("'Fechar menu'", "'Close menu'"),
    ("'Abrir menu'", "'Open menu'"),
    ('>28/09<', '>Sep 28<'),
    (' / ficha técnica', ' / tech sheet'),
    ('Baixar currículo', 'Download résumé (PT)'),
    ('rafapessoa.com.br/og-rafael-pessoa-v3.jpg', 'rafapessoa.com.br/og-rafael-pessoa-v3-en.jpg'),
]
for de, para in TRECHOS:
    assert de in s, de
    s = s.replace(de, para)
s = re.sub(r'(\d{2}/\d{4}) a (\d{2}/\d{4})', r'\1 to \2', s)
s = s.replace('01/2024 até hoje', '01/2024 to date')

T = {
 "Rafael Pessoa, Analista de Dados Sênior, Desenvolvedor Fullstack e AI Engineer em Natal/RN": "Rafael Pessoa, Senior Data Analyst, Full-stack Developer and AI Engineer in Natal, Brazil",
 "Rafael Pessoa é Analista de Dados Sênior, Desenvolvedor Fullstack Sênior e AI Engineer em Natal, Rio Grande do Norte. Modelagem e consultas em SQL, ETL e automação em Python, modelo semântico e DAX em Power BI, aplicações em produção com FastAPI e Vue, e IA dentro do produto com Claude e Gemini. Certificado Microsoft PL-300. Atende remoto em todo o Brasil.": "Rafael Pessoa is a Senior Data Analyst, Senior Full-stack Developer and AI Engineer based in Natal, Brazil. SQL modeling and queries, ETL and automation in Python, semantic models and DAX in Power BI, production applications with FastAPI and Vue, and AI inside the product with Claude and Gemini. Microsoft PL-300 certified. Available for remote work.",
 "Análise de dados de ponta a ponta em SQL, Python e Power BI, e sistemas próprios em produção com FastAPI e Vue. Natal/RN, atendimento remoto em todo o Brasil.": "End-to-end data analysis in SQL, Python and Power BI, plus my own systems in production with FastAPI and Vue. Based in Natal, Brazil, available for remote work.",
 "Rafael Pessoa, Analista de Dados Sênior, Desenvolvedor Fullstack e AI Engineer": "Rafael Pessoa, Senior Data Analyst, Full-stack Developer and AI Engineer",
 "Analista de dados sênior, desenvolvedor fullstack e AI Engineer. SQL, Python, Power BI, DAX, FastAPI, Vue, Claude, Gemini, LGPD. Natal/RN, remoto ou híbrido.": "Senior data analyst, full-stack developer and AI Engineer. SQL, Python, Power BI, DAX, FastAPI, Vue, Claude, Gemini, LGPD. Natal, Brazil, remote or hybrid.",
 "Rafael Pessoa, analista de dados sênior, desenvolvedor fullstack e AI Engineer em Natal, Rio Grande do Norte": "Rafael Pessoa, senior data analyst, full-stack developer and AI Engineer in Natal, Rio Grande do Norte, Brazil",
 "Pular para o conteúdo": "Skip to content",
 "Navegação principal": "Main navigation",
 "Sobre": "About", "Experiência": "Experience", "Projetos": "Projects", "Perguntas": "Questions", "Contato": "Contact",
 "Abrir menu": "Open menu",
 "Rafael Pessoa, Analista de Dados Sênior, Desenvolvedor Fullstack Sênior e AI Engineer em Natal. Consulta em SQL, automação em Python, modelo semântico no Power BI, a aplicação em FastAPI e Vue que produz o número, e a IA que roda dentro do produto.": "Rafael Pessoa, Senior Data Analyst, Senior Full-stack Developer and AI Engineer in Natal, Brazil. SQL queries, Python automation, semantic models in Power BI, the FastAPI and Vue application that produces the number, and the AI that runs inside the product.",
 "Ver projetos": "See projects", "Falar comigo": "Talk to me",
 "Rafael Pessoa, analista de dados sênior, desenvolvedor fullstack e AI Engineer em Natal/RN, em evento do GDG Natal": "Rafael Pessoa, senior data analyst, full-stack developer and AI Engineer in Natal, Brazil, at a GDG Natal event",
 "o que já está rodando": "what's already running",
 "sistemas próprios em produção": "of my own systems in production",
 "com dados, e com tecnologia desde 2020": "in data, and in tech since 2020",
 "pessoas no Google I/O Extended que ajudei a organizar": "people at the Google I/O Extended I helped organize",
 "Análise de dados de ponta a ponta, do SQL ao produto em produção": "End-to-end data analysis, from SQL to a product in production",
 "Trabalho com tecnologia desde 2020 e com dados desde 2024. Faço o ciclo completo da análise: modelagem e consultas em SQL, tratamento e automação em Python, construção do modelo semântico no Power BI, e a conversa com quem vai usar o número. Como desenvolvedor, mantenho aplicações próprias em produção com FastAPI e Vue, o que me obriga a pensar dado como produto e não apenas como relatório. Como AI Engineer, coloco IA dentro do produto: no ArqRede Hub, Claude e Gemini geram os relatórios em streaming, com cache de prompt, cota por ferramenta e troca de modelo quando o serviço fica cheio.": "I've worked in technology since 2020 and in data since 2024. I cover the full analysis cycle: SQL modeling and queries, Python processing and automation, building the semantic model in Power BI, and the conversation with whoever will use the number. As a developer, I maintain my own applications in production with FastAPI and Vue, which forces me to treat data as a product and not just a report. As an AI Engineer, I put AI inside the product: in ArqRede Hub, Claude and Gemini write the reports in streaming, with prompt caching, per-tool quotas and model fallback when the service is overloaded.",
 "produto em produção": "product in production",
 "Organizador do GDG Natal": "GDG Natal organizer",
 "Formação e certificação": "Education and certification",
 "Análise e Desenvolvimento de Sistemas, IFRN. Microsoft PL-300, Power BI Data Analyst Associate. Inglês B2.": "Systems Analysis and Development, IFRN. Microsoft PL-300, Power BI Data Analyst Associate. English B2.",
 "Comunidade": "Community",
 "Ajudei a organizar o Google I/O Extended e Build with AI 2026, para mais de 500 pessoas, e palestrei sobre storytelling de dados com IA.": "I helped organize Google I/O Extended and Build with AI 2026, for more than 500 people, and gave a talk on data storytelling with AI.",
 "Experiência profissional em dados e desenvolvimento": "Professional experience in data and development",
 "Cinco posições em análise de dados, business intelligence, requisitos e desenvolvimento, entre 2020 e hoje. Clique em qualquer cabeçalho para reordenar. Os percentuais ficam presos ao emprego onde aconteceram.": "Five positions across data analysis, business intelligence, requirements and development, from 2020 to today. Click any header to reorder. The percentages belong to the job where they happened.",
 "5 linhas": "5 rows", "ordene por qualquer coluna": "sort by any column",
 "Tabela de experiência profissional, rolagem horizontal": "Professional experience table, horizontal scroll",
 "Experiência profissional, ordenável por empresa, período, função, stack e resultado.": "Professional experience, sortable by company, period, role, stack and result.",
 "Empresa": "Company", "Período": "Period", "Função": "Role", "Resultado": "Result",
 "Desenvolvedor Fullstack Sênior": "Senior Full-stack Developer",
 "até hoje": "to date",
 "Plataforma de gestão de festivais em produção": "Festival management platform in production",
 "Analista de Dados Sênior": "Senior Data Analyst",
 "Visibilidade das métricas críticas, e tempo de processamento": "Visibility of critical metrics, and processing time",
 "Analista de Requisitos": "Requirements Analyst",
 "Velocidade no entendimento inicial dos projetos, e eficiência do time": "Speed in initial project understanding, and team efficiency",
 "Product Manager, estágio": "Product Manager, internship",
 "Levantamento de requisitos, backlog": "Requirements gathering, backlog",
 "Todas as sprints entregues no prazo": "All sprints delivered on time",
 "Analista de Suporte Especialista": "Support Specialist Analyst",
 "Excel, análise de logs, SLA": "Excel, log analysis, SLA",
 "Queda na reincidência de chamados": "Fewer repeat support tickets",
 "Arraste na horizontal para ver todas as colunas.": "Drag horizontally to see all columns.",
 "Confiança": "Trust",
 "Empresas, clientes e comunidade": "Companies, clients and community",
 "Onde meu trabalho já rodou e ainda roda, entre emprego, projeto de cliente e comunidade técnica.": "Where my work has run and still runs, across employment, client projects and the tech community.",
 "Empresas, clientes e comunidade com quem trabalhei": "Companies, clients and community I have worked with",
 "Destaque": "Highlight",
 "A temporada 2026 do Flamengo, jogo a jogo, em Power BI": "Flamengo's 2026 season, match by match, in Power BI",
 "Um relatório que se lê como uma reportagem: cada página responde uma pergunta sobre o ano rubro-negro.": "A report that reads like a feature story: each page answers one question about the club's year.",
 "Abrir o painel Flamengo 2026 no Power BI, em nova aba": "Open the Flamengo 2026 dashboard in Power BI, in a new tab",
 "Capa do painel Flamengo 2026: 53 jogos, 32 vitórias, 103 gols e 67,3% de aproveitamento, ao lado de fotos de três jogadores": "Cover of the Flamengo 2026 dashboard: 53 matches, 32 wins, 103 goals and a 67.3% points rate, next to photos of three players",
 "Abrir o painel": "Open the dashboard",
 "Power BI publicado": "Published in Power BI",
 "Dado de futebol costuma chegar como tabela solta de placar, e ninguém enxerga o ano inteiro de uma vez. Escrevi a coleta em Python sobre a API pública da ESPN, com resumo de cada jogo, lance a lance com coordenadas, tabela e elenco, e estimei xG e xA por distância e ângulo do chute, calibrados na própria temporada.": "Football data usually arrives as a loose table of scores, and nobody sees the whole year at once. I wrote the collection in Python on top of ESPN's public API, with a summary of every match, play-by-play with coordinates, standings and squad, and I estimated xG and xA by shot distance and angle, calibrated on the season itself.",
 "São onze capítulos, da temporada geral à reta final, passando por raio-X de cada competição, mapa de calor, quem decide e perfil individual com percentis por 90 minutos. Os filtros de competição, mês, mando e resultado valem para todos os capítulos, e o relatório inteiro é gerado por código no formato PBIP.": "There are eleven chapters, from the full season to the final stretch, covering an X-ray of each competition, heat maps, who decides matches and individual profiles with per-90 percentiles. The competition, month, home or away and result filters apply across all chapters, and the entire report is generated by code in PBIP format.",
 "API ESPN": "ESPN API",
 "Abrir o painel interativo": "Open the interactive dashboard",
 "capítulos navegáveis": "navigable chapters",
 "jogos em 6 competições": "matches in 6 competitions",
 "filtros que atravessam o relatório": "filters across the report",
 "última coleta de dados": "last data collection",
 "Painel de torcedor, sem vínculo oficial com o clube. Dados: ESPN.": "Fan-made dashboard, not officially affiliated with the club. Data: ESPN.",
 "Projetos de dados e software, do problema ao que roda hoje": "Data and software projects, from the problem to what runs today",
 "Em produção": "In production",
 "Escritórios de arquitetura perdem horas revisando prancha, conferindo norma e montando lista de compras, e o erro costuma aparecer só na obra.": "Architecture firms lose hours reviewing drawing sheets, checking codes and building shopping lists, and errors tend to surface only on site.",
 "Construí a plataforma da comunidade ArqRede, do site de venda à área logada: Analista de projetos, Corretor de pranchas e Lista de Compras, com login, pagamento, cupons e painel de vendas. Escrevi também um leitor que mede as cotas direto do desenho do PDF, sem depender de IA.": "I built the ArqRede community platform, from the sales site to the logged-in area: Project Analyst, Drawing Corrector and Shopping List, with login, payments, coupons and a sales dashboard. I also wrote a reader that measures dimensions straight from the PDF drawing, without relying on AI.",
 "Ver o Hub": "See the Hub", "Ver a ArqRede": "See ArqRede", "Abrir o ArqRede Hub": "Open ArqRede Hub",
 "Página do ArqRede Hub com o título Menos tempo perdido. Mais solução. e os cartões do Analista, do Corretor e da Lista de Compras": "ArqRede Hub page with the title Menos tempo perdido. Mais solução. and the cards for the Analyst, the Corrector and the Shopping List",
 "no ar": "live",
 "Resultado ou estado atual": "Result or current status",
 "No ar e com vendas reais, em pagamento único, ao lado do site da comunidade ArqRede.": "Live with real sales, as a one-time payment, alongside the ArqRede community site.",
 "Em lançamento": "Launching", "em lançamento": "launching",
 "Escritório de arquitetura toca projeto, comercial e financeiro em lugares separados, e fica difícil enxergar cada trabalho do orçamento à entrega.": "Architecture firms run projects, sales and finance in separate places, which makes it hard to see each job from quote to delivery.",
 "Construí a plataforma de gestão, que nasceu dentro de um escritório em operação e foi preparada para vários: esteira de projetos, comercial e financeiro conectados, com a logo e as cores de cada escritório e os dados separados por RLS no banco. Fiz também o site, com a abertura em 3D.": "I built the management platform, which started inside an operating firm and was prepared for many: project pipeline, sales and finance connected, with each firm's logo and colors and data isolated by RLS in the database. I also built the website, with a 3D opening.",
 "Ver o site": "See the site",
 "Abrir o site da BASE de Projetos": "Open the BASE de Projetos site",
 "Plataforma BASE de Projetos com a esteira de produção e o painel Perguntar, em tela de demonstração com dados fictícios": "BASE de Projetos platform with the production pipeline and the Ask panel, on a demo screen with fictional data",
 "Site no ar e plataforma em lançamento, com os escritórios parceiros Polyana Diógenes e Andreza Fama.": "Site live and platform launching, with partner firms Polyana Diógenes and Andreza Fama.",
 "Em implantação": "Rolling out", "em implantação": "rolling out",
 "Sistema da clínica Emily França": "Emily França clinic system",
 "A rotina da psicóloga passava por fichas de papel, e prontuário de paciente pede sigilo de verdade.": "The psychologist's routine ran on paper forms, and patient records demand real confidentiality.",
 "Construí o sistema da clínica para o celular e o computador: fichas, prontuário, agenda com marcação pelo próprio paciente, documentos em PDF e financeiro. Prontuário e CPF são cifrados com AES-256-GCM, e toda tabela tem RLS forçado no PostgreSQL.": "I built the clinic system for phone and desktop: patient files, clinical records, scheduling with self-booking by patients, PDF documents and finance. Records and national IDs (CPF) are encrypted with AES-256-GCM, and every table has forced RLS in PostgreSQL.",
 "Agenda semanal do sistema da clínica Emily França, com sessões de pacientes fictícios": "Weekly schedule in the Emily França clinic system, with sessions for fictional patients",
 "Publicado e em implantação com a clínica, com mais de 1.100 testes automatizados. Sistema privado, e a tela acima usa dados fictícios.": "Published and rolling out with the clinic, with more than 1,100 automated tests. Private system, and the screen above uses fictional data.",
 "O escritório atende clientes em todo o Brasil e precisava de um site que mostrasse o portfólio e levasse a pessoa direto para a conversa.": "The firm serves clients across Brazil and needed a site that showed its portfolio and took people straight to a conversation.",
 "Construí o site em Astro, com portfólio, especialidades, depoimentos e contato pelo WhatsApp. A página tem dados estruturados e llms.txt, pensados para a busca no Google e para respostas de IA.": "I built the site in Astro, with portfolio, specialties, testimonials and WhatsApp contact. The page has structured data and llms.txt, designed for Google search and AI answers.",
 "Ver no ar": "See it live",
 "Abrir o site de Andreza Fama Arquitetura": "Open the Andreza Fama Arquitetura site",
 "Página inicial do site de Andreza Fama Arquitetura com o título Do imaginário a experiências únicas e a foto de um projeto de loja": "Home page of the Andreza Fama Arquitetura site with the title Do imaginário a experiências únicas and a photo of a store project",
 "No ar no domínio do escritório, com a página de links da bio do Instagram no mesmo projeto.": "Live on the firm's domain, with the Instagram bio links page in the same project.",
 "Marcar corte dependia de mandar mensagem e esperar resposta, então a agenda vivia na cabeça de quem atendia e o cliente nunca sabia se o horário estava garantido.": "Booking a haircut meant sending a message and waiting for a reply, so the schedule lived in the head of whoever was working and the client never knew if the slot was confirmed.",
 "Construí o site de agendamento com catálogo de quinze serviços com preço e duração fechados, escolha de barbeiro e horário em quatro passos, clube de assinatura mensal e painel para a barbearia acompanhar a agenda. A entrada é por chave de acesso, sem e-mail nem senha, e quem prefere conversar marca escrevendo em texto livre no chat.": "I built the booking site with a catalog of fifteen services with fixed price and duration, barber and time selection in four steps, a monthly subscription club and a dashboard for the barbershop to follow the schedule. Sign-in is by access key, with no email or password, and anyone who prefers talking can book by typing freely in the chat.",
 "Abrir o site da Johny Barbearia": "Open the Johny Barbearia site",
 "Página inicial da Johny Barbearia com o título Sua cadeira marcada em menos de um minuto": "Johny Barbearia home page with the title Sua cadeira marcada em menos de um minuto",
 "No ar e em uso pela barbearia, em Natal, com três barbeiros na agenda e três planos do Clube Johny.": "Live and in use by the barbershop in Natal, with three barbers on the schedule and three Clube Johny plans.",
 "Organizadores de festival de dança dependiam de planilhas manuais para pontuar, ranquear e montar a ordem de apresentações.": "Dance festival organizers relied on manual spreadsheets to score, rank and build the performance order.",
 "Construí a plataforma de gestão com módulos de pontuação, ranking e ordem de apresentações, mais a automação das planilhas em Python.": "I built the management platform with scoring, ranking and performance order modules, plus spreadsheet automation in Python.",
 "ativo": "active",
 "Usada por organizadores reais. Atuo como desenvolvedor fullstack sênior e administrador.": "Used by real organizers. I work as a senior full-stack developer and administrator.",
 "Palestra": "Talk",
 "Pipeline de data storytelling com IA": "Data storytelling pipeline with AI",
 "Dado bruto de festival não vira argumento sozinho, e a leitura manual travava a conversa com quem decide.": "Raw festival data doesn't become an argument on its own, and manual reading stalled the conversation with decision makers.",
 "Montei um pipeline de cinco etapas que leva dado anonimizado até narrativa visual.": "I built a five-stage pipeline that takes anonymized data all the way to visual narrative.",
 "apresentado": "presented",
 "Virou a palestra que apresentei no Google I/O Extended 2026.": "It became the talk I gave at Google I/O Extended 2026.",
 "Entregue": "Delivered",
 "Automação de relatórios em Power BI e Python": "Report automation in Power BI and Python",
 "As extrações eram feitas à mão todo dia antes de qualquer análise começar.": "Extractions were done by hand every day before any analysis could begin.",
 "Fiz a coleta via web scraping e integração com AWS Simba, o tratamento em Pandas e NumPy, e o modelo semântico com DAX e Power Query.": "I handled collection through web scraping and AWS Simba integration, processing in Pandas and NumPy, and the semantic model with DAX and Power Query.",
 "em operação": "in operation",
 "Eliminou as extrações manuais diárias e cortou até 40% do tempo de processamento.": "Eliminated daily manual extractions and cut processing time by up to 40%.",
 "Por que fechar comigo": "Why work with me",
 "As perguntas que recrutador e gestor de dados fazem antes de me chamar para conversar.": "The questions recruiters and data managers ask before calling me for a conversation.",
 "Eu contrato um analista de dados ou um desenvolvedor?": "Am I hiring a data analyst or a developer?",
 "Os dois, na mesma pessoa. Faço consulta e modelagem em SQL, tratamento e automação em Python, o modelo semântico no Power BI, e mantenho aplicação em produção com FastAPI e Vue. Na prática, o número que eu apresento vem de um sistema que eu também sei construir e sustentar.": "Both, in the same person. I do SQL queries and modeling, Python processing and automation, the semantic model in Power BI, and I keep applications in production with FastAPI and Vue. In practice, the number I present comes from a system I also know how to build and maintain.",
 "O que você entrega chega a rodar em produção?": "Does what you deliver actually run in production?",
 "Meu time não tem engenheiro de dados. Isso trava o projeto?": "My team has no data engineer. Does that block the project?",
 "Não. Eu cubro da coleta até a entrega. Na RankMyApp a coleta vem de web scraping e integração com AWS Simba, o tratamento é em Pandas e NumPy, e o modelo semântico em Power BI com DAX e Power Query é meu. Você não precisa montar um time inteiro para começar a enxergar o dado.": "No. I cover everything from collection to delivery. At RankMyApp, collection comes from web scraping and AWS Simba integration, processing is in Pandas and NumPy, and the semantic model in Power BI with DAX and Power Query is mine. You don't need to build a whole team to start seeing your data.",
 "Como você lida com dado sensível e LGPD?": "How do you handle sensitive data and LGPD?",
 "Hoje qualquer pessoa monta dashboard e site com IA. Qual é a diferença?": "Anyone can build a dashboard or a site with AI today. What's the difference?",
 "Eu uso IA, inclusive no pipeline com Gemini e NotebookLM. A diferença é o que a IA não resolve sozinha: modelo semântico correto, controle de acesso, auditoria do que foi consultado, e alguém que responda pelo número na frente de quem vai decidir com ele. Métrica errada gerada rápido continua sendo métrica errada.": "I use AI, including in the pipeline with Gemini and NotebookLM. The difference is what AI doesn't solve on its own: a correct semantic model, access control, an audit of what was queried, and someone who answers for the number in front of the people deciding with it. A wrong metric generated quickly is still a wrong metric.",
 "Você já trabalhou fora do meu setor?": "Have you worked outside my industry?",
 "Marketing de aplicativos na RankMyApp, software de gestão na ESIG, suporte técnico em escala na Teleperformance, produto em estágio na Blacklab Ventures e festivais de dança na Dança Digital. O que se repete em todos é o mesmo trabalho: entender a regra do negócio, achar onde o dado quebra e automatizar o que era manual.": "App marketing at RankMyApp, management software at ESIG, large-scale technical support at Teleperformance, a product internship at Blacklab Ventures and dance festivals at Dança Digital. What repeats across all of them is the same work: understanding the business rule, finding where the data breaks and automating what was manual.",
 "Trabalha remoto?": "Do you work remotely?",
 "Sim, remoto ou híbrido. Base em Natal, Rio Grande do Norte. Inglês B2 para times e documentação em inglês.": "Yes, remote or hybrid. Based in Natal, Rio Grande do Norte, Brazil. English B2 for teams and documentation in English.",
 "Aberto a propostas de dados e desenvolvimento": "Open to data and development proposals",
 "E-mail": "Email", "Telefone": "Phone", "Local": "Location",
 "Natal/RN, Brasil": "Natal, RN, Brazil",
 "Rafael Pessoa, 2026. Todos os direitos reservados.": "Rafael Pessoa, 2026. All rights reserved.",
 "O estúdio de arquitetura infantil atende famílias a distância e precisava de uma página que explicasse os pacotes e levasse a família direto para a conversa.": "The children's architecture studio works with families remotely and needed a page that explained its packages and took families straight to a conversation.",
 "Construí a landing de vendas em Astro, com carrossel de abertura, quiz Monte seu universo, projetos, pacotes, Clube TumTum, perguntas frequentes e WhatsApp. A página tem dados estruturados, llms.txt e analytics que só carrega depois do consentimento de cookies.": "I built the sales landing page in Astro, with an opening carousel, the Monte seu universo quiz, projects, packages, Clube TumTum, FAQ and WhatsApp. The page has structured data, llms.txt and analytics that only loads after cookie consent.",
 "Abrir o site da TumTum": "Open the TumTum site",
 "Página inicial da TumTum com o título Crianças merecem mais que espaços comuns e a foto de uma brinquedoteca": "TumTum home page with the title Crianças merecem mais que espaços comuns and a photo of a playroom",
 "No ar no domínio do estúdio, com política de privacidade e banner de cookies.": "Live on the studio's domain, with a privacy policy and cookie banner.",
 "Landing de vendas de estúdio de arquitetura infantil, em Astro, com quiz, pacotes, dados estruturados e consentimento de cookies.": "Sales landing page for a children's architecture studio, in Astro, with a quiz, packages, structured data and cookie consent.",
 # dados estruturados
 "Empresas, clientes e comunidade com quem Rafael Pessoa trabalhou": "Companies, clients and community Rafael Pessoa has worked with",
 "Análise de dados": "Data analysis", "Modelagem de dados": "Data modeling",
 "ETL e automação de relatórios": "ETL and report automation",
 "Natal, Rio Grande do Norte, Brasil": "Natal, Rio Grande do Norte, Brazil",
 "Vagas e projetos de análise de dados, BI, desenvolvimento fullstack e IA, remoto ou híbrido": "Data analysis, BI, full-stack development and AI roles and projects, remote or hybrid",
 "Analista de Dados": "Data Analyst", "Desenvolvedor Fullstack": "Full-stack Developer",
 "SQL, Python, Power BI, DAX, Power Query, modelagem de dados, ETL, web scraping": "SQL, Python, Power BI, DAX, Power Query, data modeling, ETL, web scraping",
 "Consultoria de dados, business intelligence, desenvolvimento fullstack e IA": "Data consulting, business intelligence, full-stack development and AI",
 "Claude API, Gemini API, LLMs, streaming, prompt caching, agentes de IA": "Claude API, Gemini API, LLMs, streaming, prompt caching, AI agents",
 "Engenharia de IA": "AI engineering",
 "Brasil": "Brazil",
 "Projetos de Rafael Pessoa": "Projects by Rafael Pessoa",
 "Plataforma de soluções para escritórios de arquitetura, com Analista de projetos, Corretor de pranchas e Lista de Compras, venda online e leitor de cotas em PDF.": "Solutions platform for architecture firms, with Project Analyst, Drawing Corrector and Shopping List, online sales and a PDF dimension reader.",
 "Plataforma de gestão para escritórios de arquitetura, com esteira de projetos, comercial e financeiro conectados e dados separados por escritório.": "Management platform for architecture firms, with a project pipeline, sales and finance connected and data isolated per firm.",
 "Sistema de clínica de psicologia com fichas, prontuário cifrado, agenda, documentos em PDF e financeiro.": "Psychology clinic system with patient files, encrypted clinical records, scheduling, PDF documents and finance.",
 "Site do escritório de arquitetura comercial, em Astro, com portfólio, especialidades, depoimentos e dados estruturados.": "Website for a commercial architecture firm, in Astro, with portfolio, specialties, testimonials and structured data.",
 "Site de agendamento para barbearia em Natal, com catálogo de serviços, escolha de barbeiro e horário, clube de assinatura mensal, entrada por chave de acesso e painel de agenda.": "Booking site for a barbershop in Natal, with a service catalog, barber and time selection, a monthly subscription club, access-key sign-in and a schedule dashboard.",
 "Plataforma de gestão de festivais de dança com pontuação, ranking e ordem de apresentações, em produção.": "Dance festival management platform with scoring, ranking and performance order, in production.",
 "Disponível para novos projetos, remoto ou híbrido.": "Available for new projects, remote or hybrid.",
 "Sim, e dá para verificar. São mais de dez sistemas próprios em produção. A Dança Digital é usada por organizadores de festival, com pontuação, ranking e ordem de apresentações. O ArqRede Hub está no ar com vendas reais. Não é protótipo de portfólio, tem gente dependendo deles.": "Yes, and you can verify it. There are more than ten of my own systems in production. Dança Digital is used by festival organizers, with scoring, ranking and performance order. ArqRede Hub is live with real sales. These aren't portfolio prototypes, people depend on them.",
 "Com controle de acesso, não com confiança. No sistema da clínica Emily França, prontuário e CPF são cifrados com AES-256-GCM e toda tabela tem RLS forçado no PostgreSQL. No pipeline de storytelling o dado entra anonimizado, então a narrativa nunca depende de identificar ninguém.": "With access control, not trust. In the Emily França clinic system, clinical records and national IDs (CPF) are encrypted with AES-256-GCM and every table has forced RLS in PostgreSQL. In the storytelling pipeline the data comes in anonymized, so the narrative never depends on identifying anyone.",
 "Com controle de acesso, não com confiança. No sistema da clínica Emily França, prontuário e CPF são cifrados com AES-256-GCM e toda tabela tem RLS forçado no PostgreSQL. No pipeline de storytelling o dado entra anonimizado.": "With access control, not trust. In the Emily França clinic system, clinical records and national IDs (CPF) are encrypted with AES-256-GCM and every table has forced RLS in PostgreSQL. In the storytelling pipeline the data comes in anonymized.",
 "Os dois no mesmo profissional. Faço consulta e modelagem em SQL, tratamento e automação em Python, modelo semântico no Power BI, e mantenho aplicação em produção com FastAPI e Vue.": "Both, in the same person. I do SQL queries and modeling, Python processing and automation, the semantic model in Power BI, and I keep applications in production with FastAPI and Vue.",
 "Sim. Dança Digital é usada por organizadores de festival, e o ArqRede Hub está no ar com vendas reais.": "Yes. Dança Digital is used by festival organizers, and ArqRede Hub is live with real sales.",
 "Não. Faço a coleta, o tratamento, o modelo e a interface. Na RankMyApp a coleta vem de web scraping e integração com AWS Simba, o tratamento é em Pandas e NumPy, e o modelo semântico é meu em Power BI com DAX e Power Query.": "No. I handle collection, processing, the model and the interface. At RankMyApp, collection comes from web scraping and AWS Simba integration, processing is in Pandas and NumPy, and the semantic model in Power BI with DAX and Power Query is mine.",
 "Uso IA no pipeline de storytelling com Gemini e NotebookLM, e ainda assim o número depende de modelagem correta e de alguém que responda por ele. Meu trabalho é a camada que a IA não faz sozinha: o modelo semântico, o controle de acesso, a auditoria e a conversa com quem decide.": "I use AI in the storytelling pipeline with Gemini and NotebookLM, and the number still depends on correct modeling and on someone who answers for it. My work is the layer AI doesn't do on its own: the semantic model, access control, auditing and the conversation with decision makers.",
 "Marketing de aplicativos na RankMyApp, software de gestão na ESIG, suporte técnico em escala na Teleperformance, produto em estágio na Blacklab Ventures e festivais de dança na Dança Digital.": "App marketing at RankMyApp, management software at ESIG, large-scale technical support at Teleperformance, a product internship at Blacklab Ventures and dance festivals at Dança Digital.",
 "Sim, remoto ou híbrido. Base em Natal, Rio Grande do Norte.": "Yes, remote or hybrid. Based in Natal, Rio Grande do Norte, Brazil.",
 "Cinco etapas que levam dado anonimizado de festival até narrativa visual, com Gemini, NotebookLM e Looker Studio. Apresentado no Google I/O Extended 2026.": "Five stages that take anonymized festival data to visual narrative, with Gemini, NotebookLM and Looker Studio. Presented at Google I/O Extended 2026.",
 "Coleta por web scraping e AWS Simba, tratamento em Pandas e NumPy, modelo semântico em Power BI com DAX e Power Query.": "Collection through web scraping and AWS Simba, processing in Pandas and NumPy, semantic model in Power BI with DAX and Power Query.",
 "Relatório em Power BI com a temporada 2026 do Flamengo jogo a jogo, em onze capítulos: resultados, raio-X por competição, mapa de calor, destaques individuais e percentis por 90 minutos, com dados coletados em Python da API pública da ESPN e xG e xA estimados na própria temporada.": "Power BI report on Flamengo's 2026 season match by match, in eleven chapters: results, an X-ray of each competition, heat maps, individual highlights and per-90 percentiles, with data collected in Python from ESPN's public API and xG and xA estimated on the season itself.",
}

# um texto inteiro por vez, do maior para o menor, para um trecho curto nunca morder um longo
for pt in sorted(T, key=len, reverse=True):
    en = T[pt]
    for bruto, novo in ((pt, en), (pt.replace("'", "&#39;"), en.replace("'", "&#39;"))):
        s = re.sub(r'(?<=[>"])(\s*)' + re.escape(bruto) + r'(\s*)(?=[<"])', lambda m: m.group(1) + novo + m.group(2), s)

# caminhos: a página fica uma pasta abaixo
s = re.sub(r'(src|href)="(logos/|projetos/|destaques/|foto-rafael|CV_)', r'\1="../\2', s)

# o que ainda estiver em português para a geração
class Textos(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.fora = []; self.achados = []
    def handle_starttag(self, tag, attrs):
        if tag in ("style", "script", "noscript"): self.fora.append(tag)
        for k, v in attrs:
            if k in ("alt", "aria-label", "data-rot", "data-funcao") and v: self.achados.append(v)
            if k == "content" and v and re.search(r"[a-zà-ú]{3} ", v): self.achados.append(v)
    def handle_endtag(self, tag):
        if self.fora and self.fora[-1] == tag: self.fora.pop()
    def handle_data(self, d):
        if not self.fora and d.strip(): self.achados.append(" ".join(d.split()))

t = Textos(); t.feed(s)
for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
    def varrer(v):
        if isinstance(v, str): t.achados.append(v)
        elif isinstance(v, list): [varrer(i) for i in v]
        elif isinstance(v, dict): [varrer(i) for k, i in v.items() if k not in ("@type", "@context")]
    varrer(json.loads(m.group(1)))

# marcas, títulos citados e o nome em português que precisa ficar
NOMES = re.compile(r"Monte seu universo|Crianças merecem|Dança Digital|Diógenes|França|Menos tempo perdido|Do imaginário|Sua cadeira|Ler esta página|Barbearia|Arquitetura|BASE de Projetos|Tudo para Pet|Clube Johny|Rio Grande do Norte")
PT = re.compile(r"[ãõçáéíóúâêô]|\b(de|da|em|com|para|que|uma|não|os|na)\b", re.I)
sobrou = sorted({x for x in t.achados if PT.search(x) and not NOMES.search(x) and not re.match(r"https?:|mailto:", x) and "@" not in x and "résumé" not in x})
if sobrou:
    print("SEM TRADUÇÃO:", len(sobrou))
    for x in sobrou: print(" -", x[:150])
    sys.exit(1)

(PASTA / "en").mkdir(exist_ok=True)
(PASTA / "en" / "index.html").write_text(s, encoding="utf-8", newline="")
print("en/index.html gerado", len(s))
