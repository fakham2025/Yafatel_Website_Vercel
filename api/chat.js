export default async function handler(req, res) {
    if (req.method !== 'POST') {
        return res.status(405).json({ error: 'Method Not Allowed' });
    }

    // Récupération de la clé API depuis les variables d'environnement de Vercel
    const apiKey = process.env.OPENAI_API_KEY;

    if (!apiKey || apiKey === "VOTRE_CLE_API_OPENAI_ICI" || apiKey === "") {
        return res.status(200).json({ 
            reply: "[Mode Démo] Bonjour ! Pour activer l'intelligence artificielle sur Vercel, veuillez ajouter votre clé API OpenAI dans les 'Environment Variables' (nom: OPENAI_API_KEY) de votre projet Vercel. En attendant, n'hésitez pas à visiter notre page <a href='contact.html' style='color:#0066FF; font-weight:bold;'>Contact</a>." 
        });
    }

    const systemPrompt = `Tu es l'assistant virtuel officiel de 'Yafatel', un bureau d'études télécom basé à Tanger (Maroc). Tu t'adresses principalement à des clients professionnels B2B européens (français, belges, suisses). Ton ton doit être professionnel, courtois, expert et rassurant.
L'entreprise est spécialisée dans l'externalisation de la production d'études télécoms (FTTH, FTTX, ingénierie mobile 4G/5G) et la production de livrables sur des logiciels comme AutoCAD, QGIS, GraceTHD, Netgeo, etc. Notre atout est d'offrir des livrables de haute qualité (taux de rejet quasi nul) et une réduction des coûts (jusqu'à 30%) par rapport aux bureaux d'études européens, grâce à notre équipe d'ingénieurs au Maroc.
Tes consignes strictes (Règles de réponse) :
1. Sois concis : Fais des réponses courtes (2 à 3 phrases maximum) pour faciliter la lecture dans une petite fenêtre de chat.
2. Pas de tarification : Ne donne jamais de prix, de tarifs ou de délais précis. Si on te demande un prix, explique que chaque projet est sur mesure.
3. Reste dans le sujet : Réponds uniquement aux questions liées aux télécoms, aux bureaux d'études, ou à l'externalisation. Si la question est hors sujet, excuse-toi poliment et recadre sur les services de Yafatel.
4. Objectif Final (Conversion) : Ton but principal n'est pas de tout résoudre, mais de qualifier le prospect. À la fin de chaque conversation pertinente, tu dois obligatoirement rediriger l'utilisateur vers la page Contact (lien: contact.html) ou lui demander de laisser son email pour qu'un expert technique le rappelle.`;

    const userMessage = req.body.message || '';

    if (!userMessage) {
        return res.status(400).json({ error: 'Le message est vide.' });
    }

    const postData = {
        model: "gpt-4o-mini",
        messages: [
            { role: "system", content: systemPrompt },
            { role: "user", content: userMessage }
        ],
        temperature: 0.7,
        max_tokens: 150
    };

    try {
        const response = await fetch('https://api.openai.com/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${apiKey}`
            },
            body: JSON.stringify(postData)
        });

        const data = await response.json();

        if (response.ok) {
            const botReply = data.choices[0].message.content;
            return res.status(200).json({ reply: botReply });
        } else {
            console.error('OpenAI API Error:', data);
            return res.status(500).json({ reply: "Désolé, je rencontre un problème technique avec l'IA. Veuillez utiliser la page Contact." });
        }
    } catch (error) {
        console.error('Fetch Error:', error);
        return res.status(500).json({ reply: "Erreur de connexion au serveur d'IA." });
    }
}
