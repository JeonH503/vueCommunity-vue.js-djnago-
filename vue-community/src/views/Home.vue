<template>
  <div class="homeBody">
    <div class="newPost">
      <div class="newCommunity">
        <h3>커뮤니티</h3>
        <h5 v-for="(item,index) in this.newPost.community" v-bind:key="item.index">
          <router-link class="_postlink" :to="{path: `board/post/${item.id}`}">{{item.title}}</router-link>
          <span class="time">{{setTimeFormat(item.datetime)}}</span>
          <span class="_writer">{{item.writer}}({{item.writer_ip}})</span>
        </h5>
      </div>
      <div class="newQuestions">
        <h3>Q&A</h3>
        <h5 v-for="(item,index) in this.newPost.questions" v-bind:key="item.index">
          <router-link class="_postlink" :to="{path: `board/post/${item.id}`}">{{item.title}}</router-link>
          <span class="time">{{setTimeFormat(item.datetime)}}</span>
          <span class="_writer">{{item.writer}}({{item.writer_ip}})</span>
        </h5>
      </div>
      <div class="newCode">
        <h3><>code</h3>
        <h5 v-for="(item,index) in this.newPost.code" v-bind:key="item.index">
          <router-link class="_postlink" :to="{path: `board/post/${item.id}`}">{{item.title}}</router-link>
          <span class="time">{{setTimeFormat(item.datetime)}}</span>
          <span class="_writer">{{item.writer}}({{item.writer_ip}})</span>
        </h5>
      </div>
    </div>
    <div class="etc">
      <div class="best">
        <h3>주간 베스트</h3>
        <h5 v-for="(item,index) in this.hotPost.hot" v-bind:key="item.index">
          <router-link class="_postlink" :to="{path: `board/post/${item.id}`}">{{item.title}}</router-link>
          <span class="time">{{setTimeFormat(item.datetime)}}</span>
          <span class="_writer">{{item.writer}}({{item.writer_ip}})</span>
        </h5>
      </div>
      <div class="notice">
        <h3>공지사항</h3>
        <h5 v-for="(item,index) in this.notice.notice" v-bind:key="item.index">
          <router-link class="_postlink" :to="{path: `board/post/${item.id}`}">{{item.title}}</router-link>
          <span class="time">{{setTimeFormat(item.datetime)}}</span>
          <span class="_writer">{{item.writer}}({{item.writer_ip}})</span>
        </h5>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import moment from 'moment';
export default {
  name: 'Home',
  data(){
    return{
      newPost: [],
      hotPost: [],
      notice : []
    };
  },
  components: {
  },
  methods: {
    setTimeFormat : function (datetime) {
      return moment(datetime).format("MM.DD HH:mm")
    }
  },
  created () {
    axios.get('/board/board_list/new?cat=community')
    .then((result) => {
      this.$set(this.newPost,'community',result.data.results)
    }),
    axios.get('/board/board_list/new?cat=questions')
    .then((result) => {
      this.$set(this.newPost,'questions',result.data.results)
    }),
    axios.get('/board/board_list/new?cat=code')
    .then((result) => {
      this.$set(this.newPost,'code',result.data.results)
    })
    axios.get('/board/board_list/hot')
    .then((result) => {
      this.$set(this.hotPost,'hot',result.data.results)
    }),
    axios.get('/board/?format=json&cat=notice')
    .then((result) => {
      this.$set(this.notice,'notice',result.data.results)
    })
  }
};
</script>

<style>
  .newPost{
    margin: 50px 10px;
    display: flex;
  }

  .etc{
    margin: 50px 170px;
    display: flex;
    
  }

  .etc div {
    width: 300px;
    border: 1px solid #dcdcdc;
    border-radius: 6px;
    background-color: white;
    margin : 0 10px;
  }

  .newPost div {
    width: 300px;
    border: 1px solid #dcdcdc;
    border-radius: 6px;
    background-color: white;
    margin : 0 10px;
  }

  h5{
    margin:0;
    padding:10px 10px;
    border-top: 1px solid #dcdcdc;
    font-weight: 400;
  }

  .homeBody h5 ._writer{
    margin-right:10px; 
    float:right;
  }

  .homeBody h5 .time{
    float:right;
  }

  ._postlink{
    text-decoration: none;
    color:black;
  }

  .homeBody h3{
    margin: 7px 10px;
  }
</style>