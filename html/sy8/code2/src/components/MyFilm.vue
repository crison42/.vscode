<template>
  <h1>软工2213班常洪</h1>
  <div class="film">
    <!--电影购票左边  -->
    <div class="filmLeft">
      <h3>屏幕</h3>
      <ul>
        <li v-for="(item, index) in seatflag" :key="index" class="seat" :class="{
          noSeat: seatflag[index] == -1,
          seatSpace: seatflag[index] == 0,
          seatActive: seatflag[index] == 1,
          seatNoUse: seatflag[index] == 2,
        }" @click="handleClick(index)"></li>
      </ul>
    </div>
    <!-- 电影购票右边 -->
    <div class="filmRight">
      <div class="rightTop">
        <div class="rightTopleft">
          <a href="#">
            <img :src="filmInfo.filmImg" alt="..." height="200" />
          </a>
        </div>
        <div class="rightTopRight">
          <p>
            中文名：<strong>{{ filmInfo.name }}</strong>
          </p>
          <p>英文名：{{ filmInfo.nameEnglish }}</p>
          <p>剧情：{{ filmInfo.storyType }}</p>
          <p>版本：{{ filmInfo.copyRight }}</p>
          <p>{{ filmInfo.place }} / {{ filmInfo.timeLength }}</p>
          <p>{{ filmInfo.timeShow }}</p>
        </div>
      </div>
      <div class="rightBootom">
        <p>影院：<strong>{{ filmInfo.cinema }}</strong> </p>
        <p>影厅：<strong>{{ filmInfo.room }}</strong></p>
        <p>场次：<strong>{{ filmInfo.time }}</strong></p>
        <p id="seatSelect">
          座位：<span v-for="(item, index) in userFilmMsg.curSeatDisp" :key="index">{{
          item + " "
        }}</span>
        </p>
        <p>
          已选择<strong style="color: red">{{ userFilmMsg.count }}</strong>个座位，<strong style="color: red">再次单击座位可取消。
            <span v-if="userFilmMsg.maxFlag">您一次最多只能买五张票！</span></strong>
        </p>
        <hr />
        <p>
          单价：<strong>{{ numberFormat(filmInfo.unitPrice) }}</strong>
        </p>
        <p>
          总价：<strong style="color: red">{{ numberFormat(fileTotal) }}</strong>
        </p>
        <hr />
        <button type="button" class="btn" @click="filmSubmit">确认下单</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, computed } from "vue";
const seatflag = reactive(//0表示空座，-1表示没有座位，1表示被选中座位,2表示已购买座位
  [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0,
    2, 2, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0,
    -1, -1,
  ]
)
const filmInfo = reactive({
  name: "囧妈",
  nameEnglish: "Lost in Russia",
  copyRight: "中文2D",
  filmImg: '/src/assets/film1.png',
  storyType: "喜剧",
  place: "中国大陆",
  timeLength: "126分钟",
  timeShow: "2020.02",
  cinema: "万达影城",
  room: "8号影厅",
  time: "2021.05.18（周二）20:00",
  unitPrice: 38,
})
const userFilmMsg = reactive({
  curSeat: [],
  curSeatDisp: [],
  count: 0,
  maxLength: 5,
  maxFlag: false,
  seatCol: 10,
})
// 数据格式化方法
const numberFormat = (value) => "￥" + value.toFixed(2);

// 计算属性计算总票价
const fileTotal = computed(() => {
  return userFilmMsg.count * filmInfo.unitPrice;
});
// 单击座位事件处理方法
const handleClick = (index) => {
  if (seatflag[index] === 1) {
    seatflag[index] = 0;
    userFilmMsg.curSeat.splice(
      userFilmMsg.curSeat.findIndex((item) => item === index),
      1
    );
  } else {
    // 判断单击座位是否是可选座位并且选中座位数小于5
    if (seatflag[index] === 0 && userFilmMsg.curSeat.length < 5) {
      seatflag[index] = 1;
      userFilmMsg.curSeat.push(index);  //将选中座位的下标进行存储
    }
  }
  // 设置当前选中的座位
  userFilmMsg.curSeatDisp = [];
  for (const data of userFilmMsg.curSeat) {
    userFilmMsg.curSeatDisp.push(
      Math.floor(data / userFilmMsg.seatCol) + 1 + "行" + ((data % userFilmMsg.seatCol) + 1) + "列");
  }
  // 计数已经选择了多少个座位
  var mySeat = seatflag.filter((item) => item === 1);
  userFilmMsg.count = mySeat.length;
  // 判断达到购买上限
  if (userFilmMsg.count >= 5) userFilmMsg.maxFlag = true;
  else userFilmMsg.maxFlag = false;
}
// “确认提交”按钮
const filmSubmit = () => {
  var flag = confirm("确认提交吗？")
  if (flag) alert("已提交！")
}
</script>

<style scoped>
h1 {
  text-align: center;
}

.film {
  margin: 0 auto;
  width: 1050px;
  border: 1px solid grey;
  height: 550px;
}

.filmLeft {
  width: 550px;
  height: 500px;
  float: left;
}

.filmLeft h3 {
  text-align: center;
}

.filmLeft ul li {
  list-style: none;
}

.seat {
  float: left;
  width: 30px;
  height: 30px;
  background-color: bisque;
  margin: 5px 10px;
  cursor: pointer;
}

.seatNotice {
  float: left;
  width: 30px;
  height: 30px;
  margin: 5px 10px;
  background-color: bisque;
  list-style: none;
  margin-left: 50px;
}

.notice {
  float: left;
  height: 30px;
  line-height: 30px;
}

.filmRight {
  width: 500px;
  height: 580px;
  float: left;
  background-color: bisque;
}

.rightTopleft {
  float: left;
  margin: 20px 15px 5px 10px;
}

.rightTopRight {
  text-align: center;
  float: left;
  margin: 0px 0px 5px 5px;
}

.rightBootom {
  text-align: center;
  clear: both;
  margin: 0px 10px;
}

#filmInformation,
#filmRightTopLeft {
  float: left;
}

#filmRightBottom {
  clear: both;
}

.btn {
  margin-top: 8px;
  color: #fff;
  background-color: cadetblue;
  border: none;
  padding: 5px 10px;
}

/* 空位置 */
.seatSpace {
  background: url("/src/assets/bg.png")no-repeat 1px -29px;
}

/* 被选中座位 */
.seatActive {
  background: url("/src/assets/bg.png") 1px 0px;
}

/* 已经购买座位 */
.seatNoUse {
  background: url("/src/assets/bg.png") 1px -56px;
}

/* 没有位置 */
.noSeat {
  background: url("/src/assets/bg.png") 1px -84px;
}
</style>