'''
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=gb2312">
        <title></title>
    </head>
    <body>
        <div align="center">
        <h4>hello girl</h4>
        <input type="button" onclick="showPro()" value="输入框弹窗按钮"/>
        <input type="button" onclick="showAlert2()" value="提示弹窗按钮"/>
        <input type="button" onclick="showAlert()" value="确认弹窗按钮"/><br><br><br>
        <span id="textSpan"></span>

        </div>
    </body>
    <script>
        function showAlert(){
            document.getElementById("textSpan").innerHTML="";
            if(confirm("你是帅哥吗？")){
                document.getElementById("textSpan").innerHTML="<font style='color: red;'>您为何如此自信？</font>";
            }else{
                document.getElementById("textSpan").innerHTML="<font style='color: red;'>您为何如此谦虚？</font>";
            }

        }
        function showPro(){
            document.getElementById("textSpan").innerHTML="";
            con = prompt("输入1为强哥聪明，输入2为左哥笨");
            if(con==1){
                document.getElementById("textSpan").innerHTML="<font style='color: green;'>强哥是真聪明啊</font>";
            }else if(con==2){
                document.getElementById("textSpan").innerHTML="<font style='color: green;'>左哥是真笨啊</font>";
            }else{
                document.getElementById("textSpan").innerHTML="<font style='color: red;'>您没有按要求输入，请重新输入</font>";
            }
        }
        function showAlert2(){
            document.getElementById("textSpan").innerHTML="";
            alert("用我三世烟火，换你一世迷离");
        }
    </script>
</html>
'''