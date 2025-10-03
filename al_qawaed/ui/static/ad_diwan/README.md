# UI Styles

Basic commands to get started.

First `cd` into dir:

```console
cd al_qawaed/al_qawaed/static/ui
```

To generate the styles:

```console
npm install
cd al_qawaed/al_qawaed/static/al_qawaed
npx @tailwindcss/cli -i ../static/al_qawaed/css/al_qawaed.css -o ../static/al_qawaed/css/styles.css --cwd ../../templates -m -w
```

To format the templates:

```console
npx prettier -w ../../templates
```
