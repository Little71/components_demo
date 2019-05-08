<template>
  <div class="wrap">
    请输入文章标题：
    <input type="text" v-model="titlehandler">
    <button class="btn btn-success" @click="addOneNote">提交</button>
    <div class="mark">
      <textarea class="editor" name id cols="100" rows="10" v-model="markdownHandler"></textarea>
      <div class="show" v-html="currentValue" ref="t"></div>
    </div>
  </div>
</template>
<script>
import Marked from "marked";
export default {
  name: "Vmarked",
  data() {
    return {
      markcontent: "",
      marktitle: ""
    };
  },
  computed: {
    titlehandler: {
      set:function (newvalue) {
        this.$store.state.note.title = newvalue;
        this.marktitle = newvalue;
      },
      get:function() {
        return this.marktitle;
      }
    },
    markdownHandler: {
      set:function(newvalue) {
        this.$store.state.note.content = newvalue;
        this.markcontent = newvalue;
      },
      get:function() {
        return this.markcontent;
      }
    },
    currentValue() {
      return Marked(this.markdownHandler);
    }
  },
  methods: {
    addOneNote() {
      var json = {
        id: this.$store.state.alllist.length + 1,
        title: this.titlehandler,
        content: this.$refs.t.innerText
      };
      this.$store.dispatch("addOneNote", json);
    }
  }
};
</script>
<style>
.t {
  width: 300px;
  height: 100px;
}
.mark {
  width: 800px;
  height: 400px;
  margin: 0 auto;
}

.editor,
.show {
  float: left;
  width: 395px;
  height: 400px;
  border: 1px solid #666;
}
</style>
