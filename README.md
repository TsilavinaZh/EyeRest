
# EyeRest

**EyeRest** est une application de détection de somnolence en temps réel basée sur OpenCV. Elle surveille les yeux de l'utilisateur via la webcam et déclenche une alerte visuelle en cas de fermeture prolongée des paupières, indiquant un possible endormissement.

## Fonctionnalités

- Détection de visage et des yeux avec les classificateurs Haar.
- Suivi en temps réel de l'état des yeux.
- Alerte "ALERTE SOMMEIL" après un seuil de fermeture prolongée.
- Interface simple avec affichage du statut : `REVEILLER` ou `ENDORMI`.

## Prérequis

- Python 3
- OpenCV 
- Fichiers Haar Cascade :  
  `haarcascade_frontalface_default.xml`  
  `haarcascade_eye.xml`



Appuyez sur `q` ou `Échap` pour quitter.

---

Un outil léger, utile et intelligent pour prévenir la somnolence en toute simplicité.
