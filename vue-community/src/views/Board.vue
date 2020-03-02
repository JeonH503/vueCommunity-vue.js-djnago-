<template>
  <div class="body">
      <div class="bodyHeader">
        <p>{{this.$route.params.cat}}</p>
        <router-link :to="{path: `${this.$route.params.cat}/write`}"><button>새글작성</button></router-link>
      </div>
      <table class="table" v-if="boarddata[0]">
        <th class="id">글 번호</th>
        <th class="_title">제목</th>
        <th class="writer">글쓴이</th>
        <th class="post_hit">조회수</th>
        <th class="datetime">날짜</th>
        <template v-if="$route.params.cat !== 'notice'">
          <tr v-for="(item,index) in this.noticedata" :key="item.id">
            <td>공지사항</td>
            <td class="titletd">
              <span class="relaviteWrap">
                <span :class="{ activate : item.activate , nonactivate : !item.activate}" v-html="item.thumbnail"></span>
              </span>
              <router-link @mouseover.native="mouseOnEvent(index)" @mouseout.native="mouseOnEvent(index)" class="postlink" :to="{path: `post/${item.id}`}">{{item.title}}</router-link>
            </td>
            <td>{{item.writer}} <span class="ip">({{item.writer_ip}})</span></td>
            <td>{{item.post_hit}}</td>
            <td>{{setTimeFormat(item.datetime)}}</td>
          </tr>
        </template>
        <tr v-for="(item,index) in this.boarddata" :key="item.id">
          <td>{{item.id}}</td>
          <td class="titletd">
            <span class="relaviteWrap">
              <span :class="{ activate : item.activate , nonactivate : !item.activate}" v-html="item.thumbnail"></span>
            </span>
            <router-link @mouseover.native="mouseOnEvent(index)" @mouseout.native="mouseOnEvent(index)" class="postlink" :to="{path: `post/${item.id}`}">{{item.title}}</router-link>
          </td>
          <td>{{item.writer}} <span class="ip">({{item.writer_ip}})</span></td>
          <td>{{item.post_hit}}</td>
          <td>{{setTimeFormat(item.datetime)}}</td>
        </tr>
      </table>
      <div v-else>
        <table class="table" >
        <th class="id">글 번호</th>
        <th class="_title">제목</th>
        <th class="writer">글쓴이</th>
        <th class="post_hit">조회수</th>
        <th class="datetime">날짜</th>
      </table>
      검색 결과가 없습니다.
      </div>
      <div class="pageMoveBtn">
        <button v-if="this.$route.query.pageNo > 1" v-on:click="movePage(Math.floor($route.query.pageNo)-1)"><</button>
        <span v-if="writePageCount <= 5">
          <button v-for="item in this.pageCount" :class="{clickedBtn : pageCountBollean[item-1]}" v-on:click="movePage(item)" v-bind:key="item">{{item}}</button>
        </span>
        <span v-else-if="this.$route.query.pageNo <=3 ">
          <button v-for="(item,index) in this.pageCount.slice(0,Math.floor(this.$route.query.pageNo)+1)" :class="{clickedBtn : pageCountBollean[index]}" v-bind:key="item" v-on:click="movePage(item)">{{item}}</button>
          <button>...</button>
          <button v-on:click="movePage(pageCount.length)" :class="{clickedBtn : pageCountBollean[pageCount.length-1]}">{{this.pageCount.length}}</button>
        </span>
        <span v-else-if="this.$route.query.pageNo >= this.pageCount.length-2">
          <button v-on:click="movePage(1)">{{1}}</button>
          <button>...</button>
          <button v-for="item in this.pageCount.slice(this.pageCount.length-4)" :class="{clickedBtn : pageCountBollean[item-1]}" v-bind:key="item" v-on:click="movePage(item)">{{item}}</button>
        </span>
        <span v-else-if="this.$route.query.pageNo > 3 ">
          <button v-on:click="movePage(1)">{{1}}</button>
          <button>...</button>
          <button v-for="item in this.pageCount.slice(this.$route.query.pageNo-2,Math.floor(this.$route.query.pageNo)+1)" :class="{clickedBtn : pageCountBollean[item-1]}" v-bind:key="item" v-on:click="movePage(item)">{{item}}</button>
          <button>...</button>
          <button v-on:click="movePage(pageCount.length)">{{this.pageCount.length}}</button>
        </span>
        <button v-if="this.$route.query.pageNo <= this.pageCount.length-1" v-on:click="movePage(Math.floor($route.query.pageNo)+1)">></button>
      </div>
      <form v-on:submit.prevent="searchPost">
        <input type="text" class="searchText" ref="searchText" placeholder="검색">
        <span class="searchWrap">
          <button type="submit" class="searchBtn">
            <img src="../assets/button_search.png">
          </button>                      
        </span>
      </form>
  </div>
</template>

<script>
import axios from 'axios';
import moment from 'moment';
export default {
  name: 'Board',
  components: {
  },
  watch: {
    '$route.params.cat'(to,from){
      const URI = '/board/?format=json&page=1&cat='+this.$route.params.cat;
      axios.get(URI)
      .then((result) => {
        this.boarddata = result.data.results;
        this.postCount = result.data.count;
      })
    },
    '$route.query'(to,from){
      let URI = '/board/?format=json&page='+this.$route.query.pageNo
        +'&cat='+this.$route.params.cat;
      if(this.$route.query.search){
        URI = '/board/?format=json&page='+this.$route.query.pageNo
        +'&cat='+this.$route.params.cat + '&search='+this.$route.query.search;
      }
      axios.get(URI)
      .then((result) => {
        this.boarddata = result.data.results;
        this.postCount = result.data.count;
      })
    }
  },
  data(){
    return{
      boarddata: [],
      noticedata: [],
      postCount: 0,
      pageCount: [1],
      pageCountBollean : [],
      maxPage: 10
    };
  },
  computed: {
    writePageCount : function () {
      if(this.postCount <= this.maxPage) {
        return this.pageCount.length;
      } else {
        this.pageCount = Array(Math.ceil(this.postCount/this.maxPage)).fill().map((v,i) => i+1);   
        return this.pageCount.length;
      }
    }
  },
  methods: {
    setTimeFormat : function (datetime) {
      return moment(datetime).format("YYYY.MM.DD HH:mm:s")
    },
    mouseOnEvent : function (id) {
      let postdata = this.boarddata[id];
      postdata.activate = !postdata.activate;
      this.$set(this.boarddata, id, postdata);
    },
    movePage : function (pageNo) {
      if(this.$route.query.search){
        this.$router.push({query: { pageNo: `${pageNo}` , search: `${this.$route.query.search}`} });
      } else {
        this.$router.push({query: { pageNo: `${pageNo}` } });
      }
    },
    searchPost : function () {
      this.$router.push({query: { pageNo: `1` , search: this.$refs.searchText.value} })
    }
  },
  created () {
    if(!this.$route.query.pageNo){
      this.$router.push('?pageNo=1');
    }
    let URI = '/board/?format=json&page='+this.$route.query.pageNo
      +'&cat='+this.$route.params.cat;
    if(this.$route.query.search){
        URI = '/board/?format=json&page='+this.$route.query.pageNo
        +'&cat='+this.$route.params.cat + '&search='+this.$route.query.search;
      }
    axios.get('/board/?format=json&page=1&cat=notice')
    .then((result) => {
      this.noticedata = result.data.results;
    })
    axios.get(URI)
    .then((result) => {
      this.boarddata = result.data.results;
      this.postCount = result.data.count;
    })
  },
  beforeUpdate() {
    this.pageCountBollean = [];
    this.pageCountBollean[Math.floor(this.$route.query.pageNo)-1] = true;
  },
  updated () {
    if(!this.$route.query.pageNo){
      this.$router.push('?pageNo=1');
    }
  }
};
</script>

<style>
    table {
      text-align: center;
      width: 100%;
      border-top: 1px solid #dcdcdc;
      border-collapse: collapse;
      font-size:14px;
    }
    th, td {
      border-bottom: 1px solid #dcdcdc;
      padding: 10px;
    }

    .id{
      width: 80px;
    }

    .tag{
      width: 50px;
      text-align: center;
    }

    .table ._title{
      width: 400px;
    }

    .writer{
      width: 120px;
    }

    .post_hit{
      width:70px;
    }

    .datetime{
      width: 50px;
    }

    .ip{
      font-size: 6px;
    }

    .titletd{
      text-align: left;
    }

    .titletd img{
      width: 200px;
    }

    .relaviteWrap{
      position: relative;     
    }

    .activate{
      margin: 0px;
      padding: 0px;
      position: absolute;
      bottom: 20px;
      left: -30px;
    }
    .activate img{
      background-color: white;
      border: 1px solid gray;
      padding: 3px;
    }

    .nonactivate{
      display: none;
    }

    button {
      color: #3282b8;
      background: transparent;
      border: 3px solid #3282b8;
      border-radius: 5px;
      -webkit-transition: all 0.5s ease;
      transition: all 0.5s ease;
      -webkit-transform: translate(0, 0);
      transform: translate(0, 0);
    }

    button:hover {
      cursor: pointer;
      background: #3282b8;
      color: white;
      border: 3px solid #3282b8;
      -webkit-transition: all 0.35s ease;
      transition: all 0.35s ease;
    }

    button:active {
      -webkit-transform: translate(5px, 5px);
      transform: translate(5px, 5px);
    }

    .clickedBtn{
      background: #3282b8;
      color: white;
      border: 3px solid #3282b8;
      -webkit-transition: all 0.35s ease;
      transition: all 0.35s ease;
    }

    .bodyHeader{
      text-align: left;
      padding: 20px;
    }

    .bodyHeader button{
      float: right;
    }

    .bodyHeader p{
      font-size: 18px;
      font-weight: 500;
      display: inline;
    }

    .body{
      width:860px;
      margin: 30px 0px 0px 70px;
      text-align:center;
    }

    .pageMoveBtn{
      margin : 10px 0px;
    }

    .searchWrap{
      height: 21px;
    }
    
    .searchBtn img{
      height: 10px;
    }

    .searchBtn{
      border: 0px;
      border-radius: 0px;
      -webkit-transition: all 0s ease;
      transition: all 0s ease;
    }

    .searchBtn:hover {
      cursor: pointer;
      background: #3282b8;
      border-left: 0px solid #3282b8;
      border-right: 0px solid #3282b8;
      border-top: 2px solid #3282b8;
      border-bottom: 2px solid #3282b8;
      -webkit-transition: all 0s ease;
      transition: all 0s ease;
    }

    .searchText{
      padding:1px;
    }

    form{
      height: 23px;
    }

    .postlink{
      color: black;
      text-decoration: none;
    }
</style>