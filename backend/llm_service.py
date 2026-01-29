def generate_reply(message: str) -> str:
    msg = message.lower().strip()

    # 1️⃣ DÉTRESSE CRITIQUE
    if any(k in msg for k in [
        "suicide", "me tuer", "finir ma vie",
        "envie de mourir", "je veux mourir"
    ]):
        return (
            "Je suis vraiment désolé que tu te sentes ainsi. "
            "Tu n’es pas seul. Il est très important de parler immédiatement "
            "à un professionnel de santé ou à une personne de confiance. "
            "Si tu peux, contacte les urgences ou une ligne d’aide locale."
        )

    # 2️⃣ URGENCE ÉMOTIONNELLE
    if any(k in msg for k in [
        "angoisse", "panique", "crise",
        "très mal", "plus supporter", "débordé"
    ]):
        prompt = (
            "L'utilisateur traverse une forte détresse émotionnelle. "
            "Réponds avec beaucoup d’empathie, propose une respiration simple "
            "et pose une question ouverte."
        )

    # 3️⃣ PROBLÈME PHYSIQUE
    elif any(k in msg for k in [
        "malade", "fièvre", "douleur",
        "mal au ventre", "mal à la tête"
    ]):
        prompt = (
            "L'utilisateur décrit un problème de santé physique. "
            "Reste prudent, ne fais pas de diagnostic médical. "
            "Encourage une consultation si nécessaire."
        )

    # 4️⃣ MAL-ÊTRE GÉNÉRAL
    elif any(k in msg for k in [
        "stress", "anxieux", "triste",
        "fatigué", "déprimé", "mal"
    ]):
        prompt = (
            "L'utilisateur exprime un mal-être mental. "
            "Réponds de manière empathique, rassurante et encourageante."
        )

    # 5️⃣ CAS PAR DÉFAUT
    else:
        prompt = (
            "L'utilisateur parle librement. "
            "Réponds de manière bienveillante et ouverte."
        )

    # 🧠 APPEL LLM
    try:
        response = model.generate_content(
            f"""
            {prompt}

            Message de l'utilisateur :
            {message}
            """,
            generation_config={
                "temperature": 0.6,
                "max_output_tokens": 300
            }
        )

        return response.text.strip()

    except Exception as e:
        print("❌ Erreur Gemini :", e)
        return (
            "Je rencontre un problème technique. "
            "Si tu te sens en difficulté, n’hésite pas à contacter une personne de confiance."
        )
