export default async function handler(req, res) {
    if (req.method !== 'POST') {
        return res.status(405).json({ error: 'Method Not Allowed' });
    }

    // Récupération de la clé API depuis les variables d'environnement de Vercel
    const apiKey = process.env.GEMINI_API_KEY;

    if (!apiKey || apiKey === "VOTRE_CLE_API_GEMINI_ICI" || apiKey === "") {
        return res.status(200).json({ 
            reply: "[Mode Démo] Bonjour ! Pour activer le Chatbot IA, veuillez créer une clé API gratuite sur Google AI Studio et l'ajouter dans Vercel sous le nom 'GEMINI_API_KEY'. En attendant, n'hésitez pas à visiter notre page <a href='contact.html' style='color:#0066FF; font-weight:bold;'>Contact</a>." 
        });
    }

    const systemPrompt = `Tu es l'assistant virtuel officiel de 'Yafatel', un bureau d'études télécom basé à Tanger (Maroc). Tu t'adresses principalement à des clients professionnels B2B européens (français, belges, suisses). Ton ton doit être professionnel, courtois et expert.
L'entreprise est spécialisée dans l'externalisation de la production d'études télécoms (FTTH, FTTX, ingénierie mobile 4G/5G) et la production de livrables sur des logiciels comme AutoCAD, QGIS, GraceTHD, Netgeo, etc.
Tes consignes strictes (Règles de réponse) :
1. Sois concis : Fais des réponses courtes (2 à 3 phrases maximum).
2. Pas de tarification : Ne donne jamais de prix, de tarifs ou de délais précis.
3. Reste dans le sujet : Réponds uniquement aux questions liées aux télécoms, aux bureaux d'études, ou à l'externalisation.
4. Règle Hors-Sujet OBLIGATOIRE : Si le client te pose une question totalement hors sujet (recette de cuisine, politique, devinette, ou demande d'emploi non pertinente), tu DOIS ignorer la question et répondre EXACTEMENT avec cette phrase : "Notre équipe prend contact avec vous dans un instant."
5. Objectif Final : Pour les vraies demandes, redirige l'utilisateur vers la page Contact (lien: contact.html).`;

    const userMessage = req.body.message || '';

    if (!userMessage) {
        return res.status(400).json({ error: 'Le message est vide.' });
    }

    const postData = {
        system_instruction: {
            parts: [{ text: systemPrompt }]
        },
        contents: [{
            parts: [{ text: userMessage }]
        }],
        generationConfig: {
            temperature: 0.2,
            maxOutputTokens: 150
        }
    };

    try {
        const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${apiKey}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(postData)
        });

        const data = await response.json();

        if (response.ok && data.candidates && data.candidates.length > 0) {
            const botReply = data.candidates[0].content.parts[0].text;
            return res.status(200).json({ reply: botReply });
        } else {
            console.error('Gemini API Error:', data);
            return res.status(500).json({ reply: "Désolé, je rencontre un problème technique. Veuillez utiliser la page Contact." });
        }
    } catch (error) {
        console.error('Fetch Error:', error);
        return res.status(500).json({ reply: "Erreur de connexion au serveur d'IA." });
    }
}
