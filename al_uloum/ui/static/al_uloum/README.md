# UI Styles

Basic commands to get started.

First `cd` into dir:

```console
cd al_uloum/al_uloum/static/ui
```

To generate the styles:

```console
npm install
cd al_uloum/ui/static/al_uloum
npx @tailwindcss/cli -i ../static/al_uloum/css/app.css -o ../static/al_uloum/css/styles.css --cwd ../../templates -m -w
```

To format the templates:

```console
npx prettier -w ../../templates
```
