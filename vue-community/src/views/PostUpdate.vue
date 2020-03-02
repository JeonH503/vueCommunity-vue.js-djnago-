<template>
  <div class="writerWrap">
    <form v-on:submit.prevent="writePost">
      제목 : <input type="text" class="titleInput" ref="title" v-bind:value='this.postData.title'>
      <ckeditor ref="editor" :editor="editor" v-model="editorData" :config="editorConfig"></ckeditor>
      패스워드 : <input type="password" ref="passwordChk">
      <input class="passwordInput" type="submit" value="수정">
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
export default {
  name: 'Post',
  components: {
  },
  data(){
    return{
      postData:'',
      editor: ClassicEditor,
      editorData: '',
      editorConfig: {
        language: 'ko',
        ckfinder: {
          uploadUrl: '/imageapi/image/',
          options: {
              resourceType: 'Images'
          }
        }
      }
    };
  },
  methods: {
    writePost() {
      let title = this.$refs.title.value;
      let content = this.editorData;
      let passwordChk = this.$refs.passwordChk.value;
      if(title.length < 3 || title.length > 10) {
        alert("제목은 3자 이상 10자 이내로 입력해주세여")
        this.$refs.title.focus();
      } else if(this.editorData < 10 || this.editorData > 10000) {
        alert("내용을 10자이상 9000자 이내로 입력해주세요")
      } else {
        axios.patch(`/board/board_list/${this.postData.id}/update`,{
        title: title,
        passwordChk : passwordChk,
        content: content,
        }).then(res => {
          alert("수정 되었습니다.")
          this.$router.push('/board/post/'+res.data.id);
        }).catch((err) => {
          alert("패스워드가 일치하지 않습니다.");
          this.$refs.passwordChk.focus();
        })
      }
    }
  },
  created () {
    const URI = `/board/board_list/${this.$route.params.post_id}/?format=json`;
    axios.get(URI)
    .then((result) => {
      this.postData = result.data;
      this.editorData = result.data.content
    })
  }
};
</script>

<style>
  .writerWrap{
    background-color: white;
    border: 1px solid gray;
    border-radius: 7px;
    width:860px;
    margin: 30px 0px 0px 70px;
    height: 600px;
  }
  .ck{
    margin-bottom: 10px; 
    height:400px;
  }
  .writerWrap form{
    margin: 20px 20px;
  }

  .titleInput{
    margin-bottom: 10px;
  }
</style>