<template>
    <div class="commentBox">
        <h3>评论</h3>
        <p v-if="comment.length==0">暂无评论，我来发表第一篇评论！</p>
        <div v-else>
            <div class="comment" v-for="(item,index) in comment" v-bind:index="index" >
                <b>{{item.name}}<span>{{item.time}}</span></b>
                <p @click="changeCommenter(item.name,index)">{{item.content}}</p>
                <div v-if="item.reply.length > 0">
                    <div class="reply" v-for="reply in item.reply">
                        <b>{{reply.responder}}&nbsp;&nbsp;回复&nbsp;&nbsp;{{reply.reviewers}}<span>{{reply.time}}</span></b>
                        <p @click="changeCommenter(reply.responder,index)">{{reply.content}}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Icon from 'vue-awesome/components/Icon';

export default {
    name: 'commemtcontent',
    components: {
        Icon
    },
    data() {
        return {
            type: 0,
            name: "testname",
            commentText: "",
            comment: [
    {
        name: "有毒的黄同学",    //评论人名字
        time: "2016-08-17",    
        content: "好,讲得非常好，good",
        reply: [              //回复评论的信息，是一个数组，如果没内容就是一个空数组
            {
                responder: "傲娇的",    //评论者
                reviewers: "有毒的黄同学",         //被评论者
                time: "2016-09-05",
                content: "你说得对"
            }
        ]
      }
    ]
        }
    },
    props:{
        type: {
            default: 0
        },
        name:{
            type: String
        },
    },
    methods: {
        changeCommenter: function(name,index) {
            this.$emit("change",name,index);
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
