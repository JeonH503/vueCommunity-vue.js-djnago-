<template>
  <div class="writerWrap">
      <form v-on:submit.prevent="writePost">
        제목 : <input type="text" class="titleInput" ref="title">
        작성자 : <input type="text" ref="writer">
        비밀번호 : <input type="password" ref="password">
        <input type = "hidden" v-bind:value="$route.params.cat" ref="tag">
        <ckeditor ref="editor" :editor="editor" v-model="editorData" :config="editorConfig"></ckeditor>
        <input type="submit" value="글쓰기">
      </form>
  </div>
</template>

<script>
import axios from 'axios';
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
export default {
  name: 'PostWrite',
  components: {
  },
  methods: {
    writePost() {
      let title = this.$refs.title.value;
      let writer = this.$refs.writer.value;
      let password = this.$refs.password.value;
      let tag = this.$refs.tag.value;
      if(title.length < 3 || title.length > 10) {
        alert("제목은 3자 이상 10자 이내로 입력해주세여")
        this.$refs.title.focus();
      } else if (writer.length < 2 || writer.length > 6) {
        alert("닉네임은 2자이상 6자 이내로 입력해주세요")
        this.$refs.writer.focus();
      } else if (password.length < 2 || password.length > 6) {
        alert("비밀번호는 2자이상 6자 이내로 입력해주세요")
        this.$refs.password.focus();
      } else if(this.editorData.length < 10 || this.editorData.length > 10000) {
        alert("내용을 10자이상 9000자 이내로 입력해주세요")
      } else {
        axios.post("/board/board_list/create",{
        title: title,
        writer: writer,
        password: password,
        tag: tag,
        content: this.editorData,
        }).then(res => {
          alert("작성 되었습니다.")
          this.$router.push('/board/post/'+res.data.id);
        })
      }
      
    }
  },
  data(){
    return{
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
};
</script>

<style>
  .writerWrap form{
    margin: 20px 20px;
  }
</style>