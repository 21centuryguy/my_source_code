<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Hosting Tool</title>
    <link rel="stylesheet" type="text/css" href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css">
</head>
<body>
    <h1>My Hosting Tool</h1>
    <p>Jack's image:</p>
    <p>Before build</p>
    <br>
    <img src="/static/image_1.png" height="500" width="700" border="3"> <!-- 실제 이미지의 패스와 상관 없이 "/static/image_1.png"로 항상 고정 -->
    <br><br>
    <img src="/static/image_2.png" height="500" width="700" border="3">
    <br><br>
    <img src="/static/image_3.png" height="500" width="700" border="3">

    <br><br>
    <p>After build</p>
    <br>
    <img src="/static/image_4.png" height="500" width="700" border="3">
    <br><br>
    <img src="/static/image_5.png" height="500" width="700" border="3">
    <br><br>
    <img src="/static/image_6.png" height="500" width="700" border="3">

    <br><br>
    <a href="sub_page_1.html">sub_page_1</a> <!-- setup.py에서 처음부터 지정되지 않은 파일은 사용 할 수 없어 / html, js, css, image 등 필요한 파일들을 미리 추가 해놓으면, 형태야 어떤 식으로든 사용 할 수 있겠네 -->

</body>
</html>