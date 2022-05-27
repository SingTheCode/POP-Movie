<template>
  <div id="comment-form">
    <div id="form-title-box">
      <div id="form-title">Comment</div>
      <button @click="createComment">게시</button>
    </div>
    <textarea type="textarea" v-model.trim="comment"/>
  </div>
</template>

<script>
export default {
  name: "CommentForm",
  data() {
    return {
      comment: "",
    };
  },
  methods: {
    createComment: function () {
      const commentItem = {
        movieId: this.$route.params.id,
        userId: "spiderq10@gmail.com",
        context: this.comment,
      };

      if (commentItem.context) {
        this.$store.dispatch("createComment", commentItem);
      }
      this.comment = '';
    },
  },
};
</script>

<style scoped>
#comment-form {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  width: 100%;
  padding-bottom: 1rem;
}

#form-title-box {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 1rem;
}

#form-title {
  font-size: 24px;
}

button {
  width: 5rem;
  height: 2rem;
  background-color: #b1fd00;
  color: black;
  font-size: 0.9rem;
  font-weight: 600;
  border-style: none;
  border-radius: 8px;
}

textarea {
  height: 12vh;
}
</style>
