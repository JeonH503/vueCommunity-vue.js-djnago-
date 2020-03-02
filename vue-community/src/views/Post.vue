<template>
  <div>
    <p class="tag">{{this.postData.tag}}</p>
    <div class="postWrap" v-if="this.postData">
        <div class="postHead">
          <p class="time">{{setTimeFormat(this.postData.datetime)}}</p>
          <p class="postTitle">{{this.postData.title}}</p>
        </div>
        <div class="postbody">
          <p class="_writer">{{this.postData.writer}}({{this.postData.writer_ip}})</p>
          <p class="postHit">{{this.postData.post_hit}}</p>
          <p class="postHitImg"><img src="../assets/eye.png"/></p>
        </div>
        <p class="postContent" v-html="this.postData.content"></p>
        <button v-on:click="activateModal">삭제</button>
        <button v-on:click="updateBtn">수정</button>
        <div id="lv-container" data-id="city" data-uid="MTAyMC80ODc5Mi8yNTI4Ng=="></div>
        <div class="deleteModal" v-on:click="inactivateModal" v-bind:class="{activatedModal : inactiveModal}">
          <div class="deleteDiv">
            <form class="deleteForm" v-on:submit.prevent="deletePost">
              <span>비밀번호 : </span><input type="password" ref="password"> 
              <input type="submit" class="deletePwd" value="삭제">
            </form>
          </div>
        </div>
    </div>
    <div class="loading" v-else>
      now loading...
      <div id="lv-container" data-id="city" data-uid="MTAyMC80ODc5Mi8yNTI4Ng=="></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import moment from 'moment';
export default {
  name: 'Post',
  components: {
  },
  data(){
    return{
      postData:'',
      inactiveModal:true
    };
  },
  methods: {
    setTimeFormat : function (datetime) {
      return moment(datetime).format("YYYY.MM.DD HH:mm:s")
    },
    inactivateModal (e) {
      if(e.target.classList[0] === 'deleteModal') {
        this.inactiveModal = !this.inactiveModal;
      }
    },
    activateModal () {
      this.inactiveModal = !this.inactiveModal;
    },
    deletePost () {
      let password = this.$refs.password.value;
      const URI = `/board/board_list/${this.postData.id}/delete`;
      axios.delete(URI, {
        data:{password : password}
      })
      .then((res)=>{
        this.$router.go(-1);
      }).catch((err) => {
        alert("비밀번호 오류")
        this.$refs.password.value = '';
        this.$refs.password.focus();
      })
    },
    updateBtn () {
      this.$router.push({path : `/board/post/${this.postData.id}/update/`});
    }
  },
  async created () {
    (function(d, s) {
              var j, e = d.getElementsByTagName(s)[0];
              if (typeof LivereTower === 'function') { return; }

              j = d.createElement(s);
              j.src = 'https://cdn-city.livere.com/js/embed.dist.js';
              j.async = true;

              e.parentNode.insertBefore(j, e);
              })(document, 'script');
    const URI = `/board/board_list/${this.$route.params.post_id}/?format=json`;
    await axios.patch(`/board/board_list/${this.$route.params.post_id}/updatePostHit`)
    .then((res) => {
    });
    axios.get(URI)
    .then((result) => {
      this.postData = result.data;
    })
  },
  mounted() {
    
  }
};
</script>

<style>
  .postWrap{
    background-color: white;
    border: 1px solid gray;
    border-radius: 7px;
    width:860px;
    margin: 30px 0px 0px 70px;
    overflow: hidden;
  }
  .postHead{
    margin:0 10px;
    overflow: hidden;
    border-bottom: 1px solid rgba( 0, 0, 0, 0.3);
  }
  .postHead .postTitle{
    margin-left:10px;
    float: left;
  }
  .postHead .time{
    margin-right:10px;
    float: right;
  }

  .postbody{
    border-bottom: 1px solid rgba( 0, 0, 0, 0.3);
    overflow: hidden;
    clear: both;
    padding:0 10px;
    margin-bottom: 10px;
  }

  ._writer{
    margin-left:10px;
    float:left;
  }

  .postHit{
    margin-right:10px;
    float:right;
  }

  .postContent{
    margin: 0 30px;
    clear: both;
  }

  .postWrap button{
    margin-right:20px;
    float: right;
  }

  .postWrap .activatedModal{
    display:none;
  }

  .postWrap .deleteModal{
    text-align: center;
    max-width:none;
    max-height: 100%;
    min-width: 100%;
    min-height: 100%;
    position: absolute;
    left: 50%;
    top: 50%;
    -webkit-transform: translate(-50%,-50%);
    transform: translateX(-50%) translateY(-50%); 
    background-color: rgba(0,0,0,0.6);
  }

  .deleteDiv{
    border-radius: 15px;
    background-color: white;
    position: absolute;
    height: 300px;
    width: 400px;
    margin:-150px 0px 0px -200px;
    top: 50%;
    left: 50%;
    padding: 5px;
  }

  .deleteForm{
    position: absolute;
    top: 45%;
    left: 15%;
  }

  .deletePwd{
    color: #3282b8;
    background: transparent;
    margin: 0;
    border: 1px solid #3282b8;
    -webkit-transition: all 0.5s ease;
    transition: all 0.5s ease;
    -webkit-transform: translate(0, 0);
    transform: translate(0, 0);
  }

  .deletePwd:hover{
    cursor: pointer;
    background: #3282b8;
    color: white;
    border: 1px solid #3282b8;
    -webkit-transition: all 0.35s ease;
    transition: all 0.35s ease;
  }

  .postHitImg{
    float:right;
  }

  .postHitImg img{
    width:20px;
  }

  #lv-container{
    margin:0 20px;
  }

  .tag{
    font-size: 18px;
    font-weight: 500;
    margin-top: 50px;
    margin-left: 90px;
  }
  .postContent .image{
    margin: 0;
  }
  
  .postContent img {
    max-width: 100%;
  }

  .postContent{
    word-break: break-all;
  }

  .loading{
    margin-top: 170px;
    margin-left: 430px;
  }
</style>