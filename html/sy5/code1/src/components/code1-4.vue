<!-- 事件修饰符的使用方法 -->
<template>
    <h1 align="center">软工2213班常洪</h1>
    <!-- stop:阻止事件冒泡 -->
    <div class="inner" @click="show('洛阳', 888)">
        <button type="button" @click.stop="show('校园', 666)">单击</button>
    </div>
    <hr>
    <!-- prevent:阻止默认事件 -->
    <a href="http://www.haust.edu.cn" @click.prevent="link">河南科技大学</a>
    <hr>
    <!-- capture:实现捕获触发事件的机制 -->
    <div class="inner" @click.capture="show('洛阳', 888)">
        <button type="button" @click="show('校园', 666)">单击</button>
    </div>
    <hr>
    <!-- self:实现只有触发当前元素的时候，才会触发事件处理函数 -->
    <div class="inner" @click.self="show('洛阳', 888)">
        <button type="button" @click="show('校园', 666)">单击</button>
    </div>
    <hr>
    <!-- once:只触发一次事件处理函数 -->
    <a href="http://www.haust.edu.cn" @click.prevent.once="link">河南科技大学</a>
    <button type="button" @click.once="show('校园', 666)">单击</button>
    <hr>
    <!-- .self和.stop的区别-->
    <!-- .self只会阻止自己身上冒泡行为的触发，并不会真正阻止冒泡行为-->
    <div class="outer" @click="show('洛阳', 999)">
        <div class="inner" @click.self="show('涧西', 888)">
            <button type="button" @click="show('校园', 666)">单击</button>
        </div>
    </div>
    <hr>
    <!-- 捕获特定按键修饰符---用于修饰键盘事件的修饰符，使用它们可以捕获特定按键 -->
    <input type="text" @keyup="sayHi">
    <input type="text" @keyup.enter="sayHi" placeholder="回车键触发事件">
    <input type="text" @keyup.space="sayHi" placeholder="空格键触发事件">
    <input type="text" @keydown.delete="sayHi" placeholder="删除键触发事件">
    <input type="text" @keyup.esc="sayHi" placeholder="ESC键触发事件">
    <input type="text" @keyup.up="sayHi" placeholder="向上箭头键触发事件"><br><br>
    <!-- 捕获鼠标按键修饰符 -->
    <button @click.middle="showmsg">中间单击</button>
    <button @click.right.prevent="showmsg">右键单击</button>
</template>

<script setup>
const show = (p1, p2) => {
    alert(p1 + "牡丹花真漂亮!" + p2)
}
const link = () => {
    alert("超链接被单击了!")
}
const sayHi = () => {
    alert("你好！");
}
const showmsg = () => {
    alert('哈哈哈哈哈哈哈哈！')
}
</script>

<style scoped>
.inner {
    width: 200px;
    height: 80px;
    background-color: pink;
}

div.sc {
    width: 200px;
    height: 200px;
    background-color: red;
    overflow: scroll;
}
</style>