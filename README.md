주소 http://ec2-15-164-104-153.ap-northeast-2.compute.amazonaws.com/<br/>
프론트 엔드 Vue.js<br/>
백엔드 djnago rest framework Rest API<br/>
배포 AWS EC2 ubuntu<br/>

기능<br/>
  1.게시판<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;● 게시판의 CRUD<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;● 게시글 삭제는 Modal Window로 구현<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;● 주간 순위<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;● 각 게시판의 신규 게시글 메인화면에 표시<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;● 공지사항에 글 작성시 각 게시판 가장 위에 표시<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;● 게시판 페이징 구현<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;● CkEditor & CkFinder 를 통한 게시글 작성, 이미지 삽입 구현<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;● 게시글 검색기능 구현<br/>

  5.댓글<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;● LiveRe를 이용한 댓글 시스템 구현<br/>
  
사용한 DBMS : MySql<br/>

라우팅 : vue router<br/>


이사이트는 프론트 엔드로는 vue.js 백엔드로 django rest framework를 이용해 Rest API를 구현 했습니다<br/>
기본적으로 익명 게시판 이지만 작성자의 각 게시글마다 작성자의 IP의 일부가 같이 표기 됩니다<br/>
글작성은 Ckeditor와 CkFinder를 이용해 구현 했으며 이미지를 업로드 하면 django의 media폴더로 업로드 됩니다<br/>
게시글 삭제버튼을 누르면 비밀번호를 입력하기 위한 Modal Window가 표시됩니다<br/>
게시글 검색기능이 구현 됐으며 작성자 이름, 제목, 내용과 검색 값이 부분 일치하는게 있다면 화면에 표시해 줍니다<br/>
공지사항의 경우 미리 설정된 비밀번호를 입력하지 않으면 작성되지 않습니다<br/>
댓글은 LiveRe를 사용했습니다<br/>


