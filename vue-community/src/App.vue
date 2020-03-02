<template>
  <div class="wrap">
    <div class="main">
      <Header></Header>
      <router-view></router-view>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from './components/Header';
import Footer from './components/Footer';
export default {
  name: 'App',

  components: {
    Header,
    Footer
  },

  data(){
    return{};
  },
};
</script>
<style>
  .wrap{
    height: 100%;
    margin-left: 170px;
  }
  .main{
    display:flex;
    height: 80%;
  }
  body{
    background-color: #f9f7f7;
  }
</style>