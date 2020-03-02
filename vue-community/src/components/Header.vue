<template>
  <div class="nav">
    <p class="title"><router-link :to="{path: `/`}" class="homeLink">MyVC</router-link></p>
    <ul class="navlist">
      <router-link v-for="(item,index) in navlist" 
        v-bind:class="{ activate: item.activate }"
        v-bind:key="index" 
        :to="{path: `/board/${item.value}?pageNo=1`}" 
        class="link">
        {{item.name}}
      </router-link>
    </ul>
  </div>
</template>

<script>
export default {
  components: {
  },
   methods: {
    moveCat : function (cat) {
      this.$router.push({ name: 'Board', params: { cat: cat }})
    }
  },
  data(){
    return{
      navlist: [
        {
          "name" : "공지사항",
          "value" : "notice"
        },
        {
          "name" : "커뮤니티",
          "value" : "community"
        },
        {
          'name' : "Q&A",
          "value" : "questions"
        },
        {
          "name" : "<>code",
          "value" : "code"
        }
      ]
    };
  },
};
</script>

<style>
  .nav{
    padding:0px;
    width: 170px;
    text-align: center;
    margin: 0px;
    background-color: #3282b8;
    position: fixed;
    top:0px;
    left: 0px;
    height: 100%;
  }
  .navlist{
    margin-top:100px;
    padding:0;
  }
  .navlist a {
    display: block;
    padding : 10px 0;
    cursor: pointer;
    list-style-type : none;
    text-decoration: none;
    color : white;
  }

  .navlist :hover{
    background-color: #0f4c75;
  }

  .title{
    cursor: pointer;
    font-size: 26px;
    font-weight: bold;
    color: white;
  }

  .title .homeLink{
    cursor: pointer;
    font-size: 26px;
    font-weight: bold;
    color: white;
  }

  .homeLink{
    text-decoration: none;
  }

  .navlist .router-link-active{
    background-color: #0f4c75;
  }
</style>