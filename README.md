# Sito vetrina AMS — come pubblicarlo (gratis, ~5 minuti)

Il sito è statico: un solo `index.html` + le immagini in `img/`. Si pubblica su
**GitHub Pages** (gratuito, sempre attivo, dominio personalizzabile in seguito).

## 1 · Copia gli screenshot (30 secondi)
Da `acm-app\docs\shots\` copia questi 5 file dentro `acm-app\website\img\`:
- `02-ops-dashboard.png`
- `06-ops-inventory-grid.png`
- `12-ops-studio.png`
- `24-portal-proposed-pending.png`
- `26-supplier-home.png`

(Se ne manca qualcuno il sito funziona lo stesso: le immagini mancanti spariscono da sole.)

## 2 · Repository separato e PUBBLICO
1. GitHub Desktop → **File → Add local repository** → scegli la cartella `acm-app\website`
2. Clicca **"create a repository here instead"** → nome `ams-site` → Create Repository
3. **Commit to main** → **Publish repository** → **TOGLI la spunta "Keep this code private"**
   (Pages gratuito richiede repo pubblico — qui c'è solo il sito, nessun codice del prodotto)

## 3 · Attiva GitHub Pages
1. Vai su github.com → repository `ams-site` → **Settings → Pages**
2. Source: **Deploy from a branch** → Branch: `main` / `(root)` → **Save**
3. Dopo ~1 minuto il sito è su: `https://TUOUSERNAME.github.io/ams-site/`

## 4 · Collega la demo live
Nel file `index.html` c'è un bottone "Try it live" con link `#DEMO_URL`:
sostituiscilo con l'URL della tua demo (Replit) quando vuoi attivarlo,
oppure dillo a Claude che lo fa lui.

## Aggiornamenti futuri
Modifica → GitHub Desktop → Commit → Push. Pages si aggiorna da solo in ~1 minuto.

## Dominio personalizzato (quando vorrai)
Compra il dominio (es. su OVH/Namecheap) → Settings → Pages → Custom domain →
segui le istruzioni DNS. Il sito resta gratis, paghi solo il dominio (~15€/anno).
