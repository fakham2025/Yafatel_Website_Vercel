import os

directory = r"C:\Users\HP\Desktop\Top skills busnesse\Site Web Vitrine wordpresse\Yafatel_Website_Vercel"

template_header = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Yafatel</title>
    <meta name="description" content="{desc}">
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Montserrat:wght@500;600;700;800&display=swap" rel="stylesheet">
    
    <!-- Icons (Phosphor Icons) -->
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
    
    <!-- Styles -->
    <link rel="stylesheet" href="css/style.css">

    <!-- OpenGraph SEO Tags -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:url" content="https://yafatel.com/{filename}">
    <meta property="og:type" content="website">
    <link rel="icon" type="image/png" href="favicon.png">
</head>
<body>

    <!-- Header / Navigation -->
    <header>
        <div class="container nav-container">
            <a href="index.html" class="logo"><span style="color: #0066FF; font-weight: 900; font-size: 1.4em;">Y</span>afatel</a>
            <nav>
                <ul class="nav-links">
                    <li><a href="index.html">Accueil</a></li>
                    <li><a href="services.html" class="active">Services</a></li>
                    <li><a href="expertise.html">Notre Expertise</a></li>
                    <li><a href="projets.html">Projets</a></li>
                </ul>
            </nav>
            <div class="nav-actions">
                <a href="contact.html" class="btn btn-primary"><span class="desktop-text">Demander un devis</span><span class="mobile-text">Devis</span></a>
            </div>
            <div class="menu-toggle">
                <i class="ph ph-list"></i>
            </div>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero" style="padding-top: 150px; padding-bottom: 80px; text-align: center;">
        <div class="container">
            <span class="section-subtitle text-accent">{subtitle}</span>
            <h1 style="max-width: 900px; margin: 0 auto 1.5rem auto;">{h1}</h1>
            <p style="max-width: 700px; margin: 0 auto 2rem auto;">{hero_desc}</p>
        </div>
    </section>
    
    <!-- Main Content -->
    <section class="section">
        <div class="container">
            {content}
        </div>
    </section>
"""

template_footer = """
    <!-- Pre-Footer CTA -->
    <section class="cta-section">
        <div class="container">
            <h2>Prêt à sécuriser votre ingénierie et réduire vos risques opérationnels ?</h2>
            <p>Demandez un audit gratuit de votre charge d'ingénierie et obtenez une simulation de réduction de coûts en 48h.</p>
            <a href="contact.html" class="btn btn-outline" style="background-color: var(--white); color: var(--primary);">Audit technique gratuit</a>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <a href="index.html" class="logo" style="margin-bottom: 1.5rem; display: block;"><span style="color: #0066FF; font-weight: 900; font-size: 1.4em;">Y</span>afatel</a>
                    <p style="max-width: 300px; margin-bottom: 1.5rem;">L'extension stratégique de votre bureau d'études télécom, basée à Tanger au Maroc. Spécialiste de l'externalisation de charge d'ingénierie.</p>
                </div>
                <div class="footer-col">
                    <h4>Piliers d'Expertise</h4>
                    <ul class="footer-links">
                        <li><a href="ftth-fttx-engineering.html">Ingénierie FTTH / FTTX</a></li>
                        <li><a href="ingenierie-reseau-mobile-4g-5g.html">Ingénierie 4G / 5G</a></li>
                        <li><a href="dao-sig-telecom.html">Expertise DAO / SIG</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Entreprise</h4>
                    <ul class="footer-links">
                        <li><a href="externalisation-bureau-etude-telecom.html">Pourquoi Externaliser ?</a></li>
                        <li><a href="projets.html">Études de Cas (ROI)</a></li>
                        <li><a href="contact.html">Nous contacter</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Yafatel. Tous droits réservés.</p>
                <div class="social-links">
                    <a href="https://www.linkedin.com/company/yafatel/" target="_blank" style="color: white; font-size: 1.5rem;"><i class="ph ph-linkedin-logo"></i></a>
                </div>
            </div>
        </div>
    </footer>

    <script src="js/main.js"></script>
</body>
</html>
"""

pages = [
    {
        "filename": "externalisation-bureau-etude-telecom.html",
        "title": "Externalisation Bureau d'Étude Télécom (B2B)",
        "desc": "Externalisation de bureau d'étude télécom au Maroc. Réduisez vos coûts d'ingénierie et vos délais de livraison tout en garantissant la conformité opérateur.",
        "subtitle": "Master Page : Externalisation",
        "h1": "Externalisation de Bureau d'Étude Télécom : Accélérez votre Production",
        "hero_desc": "Transformez vos goulets d'étranglement en avantage concurrentiel. Notre équipe délocalisée à Tanger absorbe votre charge documentaire sans faille.",
        "content": "<h2>Les enjeux de la production télécom en France</h2><p>Le marché français souffre d'une pénurie chronique de dessinateurs-projeteurs et d'ingénieurs qualifiés...</p>"
    },
    {
        "filename": "ftth-fttx-engineering.html",
        "title": "Ingénierie Réseau FTTH / FTTX (Sous-traitance B2B)",
        "desc": "Confiez vos études FTTH (APS, APD, DOE, piquetage) à nos ingénieurs télécom. Qualité GraceTHD garantie, taux de rejet opérateur 0%.",
        "subtitle": "Master Page : Expertise Fibre",
        "h1": "Sous-traitance d'Ingénierie FTTH / FTTX",
        "hero_desc": "Sécurisez vos déploiements fibre optique avec des livrables parfaits, produits dans les délais exigés par les opérateurs (Orange, SFR, Free, Bouygues).",
        "content": "<h2>Notre maîtrise des processus FTTH</h2><p>Nous réalisons l'ingénierie complète de la boucle locale optique...</p>"
    },
    {
        "filename": "pour-operateurs.html",
        "title": "Externalisation pour Opérateurs Télécoms",
        "desc": "Solutions d'ingénierie télécom dédiées aux Opérateurs d'Infrastructures. Scalabilité immédiate et gestion du risque de déploiement.",
        "subtitle": "Support Cible : Opérateurs",
        "h1": "Sécurisez les Déploiements de votre Réseau en Propre",
        "hero_desc": "Réduisez le risque opérationnel sur vos plaques FTTH/Mobile grâce à une équipe d'ingénierie offshore dédiée aux standards de votre SI.",
        "content": "<h2>Conformité et gestion du risque</h2><p>Nous savons que la continuité de service et la data qualité sont vos priorités absolues...</p>"
    },
    {
        "filename": "pour-integrateurs.html",
        "title": "Externalisation pour Intégrateurs & Sous-traitants",
        "desc": "Vous êtes sous-traitant télécom ? Externalisez vos livrables documentaires pour augmenter votre marge brute sur chaque chantier.",
        "subtitle": "Support Cible : Intégrateurs",
        "h1": "Augmentez votre Marge Brute sur les Chantiers Télécoms",
        "hero_desc": "Concentrez vos équipes internes sur le terrain et la gestion de projet. Nous gérons la production des études (APS/APD/DOE) en back-office.",
        "content": "<h2>Le défi de la rentabilité des intégrateurs</h2><p>Les prix tirés vers le bas par le marché STOC obligent à optimiser les coûts documentaires...</p>"
    },
    {
        "filename": "externalisation-telecom-france.html",
        "title": "Bureau d'étude télécom France (Partenaire Offshore)",
        "desc": "Yafatel accompagne les bureaux d'études et entreprises télécoms en France pour la conception de réseaux très haut débit et mobile.",
        "subtitle": "Support Géo : Marché Français",
        "h1": "Partenaire des Bureaux d'Études Télécoms Français",
        "hero_desc": "La rigueur de l'ingénierie française alliée à la compétitivité d'un centre de production nearshore basé à Tanger.",
        "content": "<h2>Alignement total sur le cahier des charges français</h2><p>Nos équipes maîtrisent les spécificités réglementaires locales (GraceTHD, formats de rendu régionaux)...</p>"
    },
    {
        "filename": "bureau-etude-telecom-maroc.html",
        "title": "Ingénierie Télécom Offshore au Maroc | Yafatel",
        "desc": "Centre de services IT et ingénierie télécom basé à Tanger (Maroc). Le hub offshore d'excellence pour la sous-traitance de vos études.",
        "subtitle": "Support Géo : Production Maroc",
        "h1": "Votre Centre d'Ingénierie Télécom au Maroc",
        "hero_desc": "Situé à Tanger, notre centre d'expertise offre des infrastructures sécurisées et un vivier d'ingénieurs d'élite francophones.",
        "content": "<h2>Pourquoi choisir Tanger pour votre nearshoring ?</h2><p>Proximité culturelle, vivier de talents issus des meilleures écoles, et infrastructures ultra-connectées...</p>"
    }
]

for page in pages:
    filepath = os.path.join(directory, page['filename'])
    html_content = template_header.format(**page) + template_footer
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)

print("Silo HTML files generated successfully.")
