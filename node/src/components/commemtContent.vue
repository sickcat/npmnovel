<template>
    <div class="commentBox">
        <h3>发表评论</h3>
        <b v-if="type">你回复&nbsp;{{name}}</b>
        <textarea name="" value="请填写评论内容" v-model="commentText"></textarea>
        <button class="btn" @click="addComment">发表</button>
        <button class="btn" @click="canelComment">取消</button>
    </div>
</template>

<script>
import Icon from 'vue-awesome/components/Icon';

export default {
    name: 'commemtContent',
    components: {
        Icon
    },
    data() {
        return {
            type: 1,
            name: "testname",
            commentText: "",
        }
    },
    props:{
        type: {
            default: 1
        },
        name:{
            type: String
        },
    },
    methods: {
        addComment: function() {
            this.$emit("submit",this.commentText);
            this.commentText = "";
        },
        canelComment: function() {
            this.$emit("canel");
            this.commentText = "";
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
header {
    z-index: 2;
    position: fixed;
    top: 0;
    left: 0;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 100vw;
    height: 3rem;
    line-height: 3rem;
    background: #005390;
    color: #ffffff;
}

header a{
    color: #ffffff;
}

.header-text {
    position: absolute;
    left: 0;
    display: flex;
    justify-content: center;
    width: 100%;
}

.fa-icon {
    height: 3rem;
    width: 1rem;
    margin-left: 1rem;
    margin-right: .5rem;
}
.operation{
    z-index:10;
    margin-right: 1rem;
}
.headText {
    font-size: 1.1rem !important;
}
</style>
