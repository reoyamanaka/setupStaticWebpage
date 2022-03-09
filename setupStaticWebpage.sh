#! /bin/bash


mkdir projectFolder
cd projectFolder

mkdir js
mkdir css
touch css/style.scss
touch js/main.js


touch index.html

cat > index.html << EOF

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset='UTF-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Document</title>
    <link rel='stylesheet' href='./css/style.css' />
</head>
<body>
    Your content goes here!
    <script src='./js/main.js'></script>
</body>
</html>

EOF

touch compileStyle.sh
chmod +x compileStyle.sh
cat > compileStyle.sh << EOF

#! /bin/bash


sass css/style.scss css/style.css

EOF

