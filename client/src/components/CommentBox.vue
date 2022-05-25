<template>
  <div id="comment-box">
    <CommentList/>
  </div>
</template>

<script>
import CommentList from "@/components/CommentList";

export default {
  name: "CommentBox",
  components: {
    CommentList,
  }
}
</script>

<style scoped>
#comment-box {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding: 5rem 0;
}
</style>