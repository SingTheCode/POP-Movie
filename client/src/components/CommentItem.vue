<template>
  <div id="comment-item">
    <div id="user-id">{{ userId }}</div>
    <div id="user-context">{{ context }}</div>
    <hr>
  </div>
</template>

<script>
export default {
  name: "CommentItem",
  props: {
    userId: String,
    context: String,
  }
}
</script>

<style scoped>
#comment-item {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  width: 100%;
  text-align: left;

}

#user-id {
  padding-bottom: 1rem;
}

hr {
  width: 100%;
}
</style>