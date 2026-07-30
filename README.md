# Emotion Detector

## Description

Emotion Detector est une application web basée sur Python et Flask qui utilise la bibliothèque Watson NLP pour analyser un texte et détecter les émotions exprimées.

L'application identifie les émotions suivantes :

- Joie (Joy)
- Colère (Anger)
- Tristesse (Sadness)
- Peur (Fear)
- Dégoût (Disgust)

L'émotion dominante est également déterminée et affichée à l'utilisateur.

## Fonctionnalités

- Analyse des émotions à partir d'un texte saisi par l'utilisateur.
- Utilisation de l'API Watson NLP.
- Interface web développée avec Flask.
- Gestion des erreurs pour les entrées invalides.
- Tests unitaires automatisés.
- Analyse statique du code avec Pylint.

## Structure du projet

```text
.
├── EmotionDetection
│   ├── __init__.py
│   └── emotion_detection.py
├── static
├── templates
│   └── index.html
├── server.py
├── test_emotion_detection.py
└── README.md