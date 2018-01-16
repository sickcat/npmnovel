<template>
    <div id="container" class="container" :class="backgroundClass + ' ' +colorClass + ' ' + fontFamily">
        <div class="head" v-if="operation">
            <span class="arrow-left" @click="$router.push(preView)">
                <Icon type="arrow-left-c"></Icon>
            </span>
            {{$store.state.bookInfo.title}}
        </div>
        <pulse-loader :loading="loading" :color="color" :size="size" :margin="margin"></pulse-loader>

        <v-touch class="content" v-show="!loading" @tap="operationAction($event)" :class="backgroundClass + ' ' +colorClass + ' ' + fontFamily" @doubletap="dbclickEvent()">
            <!--header>{{bookChaptersContent.title}}</header-->
            <article :class='fontFamily' id="fontStyle" v-html="bookChaptersBody" :fontFamily="fontFamily"></article>
            
            <br>
            <br>
            <div class='mulucenter'>点击底部阅读下一章</div>
            <br>
            <br>
            <br>
        </v-touch>
        <div class="setting" v-if="setting">
            <v-touch class="menu-btn middle-menu" id='autoread' @tap="auto_read()">
                <Icon type="ios-play-outline"></Icon>
                自动阅读
            </v-touch>
            <v-touch class="middle-menu menu-btn m-border" @tap="add_speed(1)">
                滚动速度+
            </v-touch>
            <v-touch class="menu-btn m-border middle-menu" @tap="add_speed(-1)">
                滚动速度-
            </v-touch>
        </div>
        <div class="setting2" v-if="setting">
            <div class="menu-btn">
                字号：
            </div>
            <v-touch class="menu-btn font-border" @tap="add_fontsize(1)">
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Aa&nbsp;&nbsp;&nbsp;+&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            </v-touch>
            <div class="menu-btn">
                {{fontSize.toFixed(1)}}
            </div>
            <v-touch class="menu-btn font-border" @tap="add_fontsize(-1)">
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Aa&nbsp;&nbsp;&nbsp;-&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            </v-touch>  
        </div>
        

        <!--div class="setting" v-if="setting">
            <v-touch class="menu-btn" @tap="auto_read()">
                <Icon type="ios-clock-outline"></Icon>
                <span>定时翻页</span>
            </v-touch>
            <v-touch class="menu-btn" @tap="add_fontsize(1)">
                <Icon type="ios-up-outline"></Icon>
                <span>字体+</span>
            </v-touch>
            <v-touch class="menu-btn" @tap="add_fontsize(-1)">
                <Icon type="ios-down-outline"></Icon>
                <span>字体-</span>
            </v-touch>
            <v-touch class="menu-btn" @tap="add_speed(1)">
                <Icon type="ios-down-outline"></Icon>
                <span>滚动速度+</span>
            </v-touch>
            <v-touch class="menu-btn" @tap="add_speed(-1)">
                <Icon type="ios-down-outline"></Icon>
                <span>滚动速度-</span>
            </v-touch>
        </div-->
        <!--div class="setting2" v-if="setting">
            <v-touch class="menu-btn">
                <span>背景颜色</span>
            </v-touch>
            <v-touch class="menu-btn" @tap="change_back(0)">
                <span class='circle background-0'>
                </span>  
            </v-touch>
            <v-touch class="menu-btn" @tap="change_back(1)">
                <span class='circle background-1'>
                </span>  
            </v-touch>
            <v-touch class="menu-btn" @tap="change_back(2)">
                <span class='circle background-2'>
                </span>  
            </v-touch>
            <v-touch class="menu-btn" @tap="change_back(3)">
                <span class='circle background-3'>
                </span>  
            </v-touch>
            <v-touch class="menu-btn" @tap="change_back(4)">
                <span class='circle background-4'>
                </span>  
            </v-touch>
        </div-->
        <div class="setting3" v-if="setting">
            <v-touch class="menu-btn">
                背景:
            </v-touch>
            <v-touch class="menu-btn" @tap="change_color(0)">
                <div class='circle color-back-0'>
                Aa
                </div>  
            </v-touch>
            <v-touch class="menu-btn" @tap="change_color(1)">
                <div class='circle color-back-1'>
                Aa
                </div>  
            </v-touch>
            <v-touch class="menu-btn" @tap="change_color(2)" style="background: #FFFFFF;">
                <div class='circle color-back-2'>
                Aa
                </div>  
            </v-touch>
            <v-touch class="menu-btn" @tap="change_color(3)">
                <div class='circle color-back-3'>
                Aa
                </div>  
            </v-touch>
            <v-touch class="menu-btn" @tap="change_color(4)">
                <div class='circle color-back-4'>
                Aa
                </div>  
            </v-touch>
        </div>
        <div class="setting4" v-if="false">
            <v-touch class="menu-btn" @tap="">
                <span>字体选择</span>
            </v-touch>
            <v-touch class="menu-btn heiti" @tap="update_family('heiti')">
                <span class="heiti">黑体</span>
            </v-touch>
            <v-touch class="menu-btn songti" @tap="update_family('songti')">
                <span>宋体</span>
            </v-touch>
            <v-touch class="menu-btn kaiti" @tap="update_family('kaiti')">
                <span>楷体</span>
            </v-touch>
            <v-touch class="menu-btn" @tap="">
                <span>定时翻页</span>
            </v-touch>
        </div>

        <div class="menu" v-if="operation">
            <v-touch class="menu-btn" @tap="showChapter">
                <Icon type="ios-list-outline"></Icon>
                目录
            </v-touch>
            <v-touch class="menu-btn" @tap="returnPos()">
                <Icon type="ios-clock-outline"></Icon>
                回到历史位置
            </v-touch>
            <v-touch class="menu-btn" v-if="nightMode" @tap="changeMode">
                <Icon type="ios-sunny-outline"></Icon>
                日间模式
            </v-touch>
            <v-touch class="menu-btn" @tap="changeMode" v-else>
                <Icon type="ios-moon-outline"></Icon>
                夜间模式
            </v-touch>
            <v-touch class="menu-btn" @tap="settings">
                <Icon type="settings"></Icon>
                设置
            </v-touch>
        </div>
        <div class="chapter-list" v-show="isShowChapter" v-scroll="onScroll">
            <div class="chapter-contents">
                <p>{{$store.state.bookInfo.title}}：目录</p>
                <v-touch tag="span" class="chapter-sort" @tap="descSort">
                    <Icon type="arrow-down-b" v-if="!chapterDescSort"></Icon>
                    <Icon type="arrow-up-b" v-else></Icon>
                </v-touch>
            </div>
            <ul class="scroll-style">
                <v-touch tag="li" v-if="loadedChapters" v-for="(chapter, index) in loadedChapters" :key="index" :class="{ selected: index==currentChapter}">
                <v-touch v-if="chapter.click" @tap="jumpChapter(index)">
                    <div class="title">&nbsp;·&nbsp;{{chapter.title}}</div>
                    <div class="title2">&nbsp;&nbsp;&nbsp;{{chapter.title2}}</div>
                </v-touch>
                <div v-else class="mulucenter">
                    {{chapter.title}}
                </div>
                </v-touch>
            </ul>
        </div>

        <Modal v-model="showAddToShelf" title="添加到书架" :closable="false" :mask-closable="false" okText="添加" @on-ok="addBook" @on-cancel="dontAddBookToShelf">
            <p>是否将该书添加到本地书架</p>
        </Modal>
    
    </div>
</template>

<script>
import api from '../libs/api'
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'

export default {
    name: 'ReadBook',
    components: {
        PulseLoader
    },
    data() {
        return {
            loading: true,
            color: '#04b1ff',
            size: '10px',
            margin: '4px',
            bookDetail: {},
            bookOrigin: {},
            bookChapter: {},
            busy: false,
            bookChaptersContent: '',
            loadedChapters: [], //缓存滚动加载的章节列表
            loadPages: 1, //滚动加载的记次
            loadedChapterContent: [], //缓存的章节内容
            preView: '', //返回上级路径
            firstLoad: true, //首次加载标识符
            operation: true, //显示操作界面标识符
            currentChapter: 0,
            isNewset: false, //最新章节
            nightMode: false, //夜间/日间模式却换
            isShowChapter: false, //是否显示目录
            showAddToShelf: false, //显示添加书架的提示
            chapterDescSort: false, //是否降序排列
            dontAddBook: false, //不添加到书架
            title: '',
            TOP: 0,
            backgroundClass: '',
            colorClass: '',
            setting: false,
            fontSize: 1.5,
            showNextTitle: true,
            dbflag: false,
            timer: Object(),
            speed: 5,
            fontFamily: 'STKaiti',
            autoread: false,
        }
    },
    computed: {
        bookChaptersBody() {
            return this.bookChaptersContent.body
            return this.bookChaptersContent && this.bookChaptersContent.body.replace(/\n/g, '<br>').replace(/(<br>.*?$<br>)/g, "<br>$").replace(/(<head>.*<\/head>)/i, "");
            //return this.bookChaptersContent && this.bookChaptersContent.body;
        },
    },
    created() {
        let readRecord = JSON.parse(window.localStorage.getItem('followBookList'));
        //let scrollTop = readRecord ? readRecord[this.$route.params.bookId].readPos : 0;
        this.firstLoad = true;
        api.getMixChapters(this.$route.params.bookId).then(response => {
            //console.log(response.data)
            this.bookChapter = response.data;
            //缓存时默认取前50章节
            //console.log(this.loadedChapters)
            if (this.$route.params.chapterId) {
                this.currentChapter = parseInt(this.$route.params.chapterId)
            }
            else {
                this.currentChapter = readRecord && readRecord[this.$route.params.bookId] && readRecord[this.$route.params.bookId].chapter ? readRecord[this.$route.params.bookId].chapter : 0;
            }
            this.loadedChapters = this.bookChapter.chapters;
            this.getBookChapterContent();
        }).catch(err => {
            console.log(err);
        })
        let settings = JSON.parse(window.localStorage.getItem('settings'));
        if (settings) {
            this.speed = settings["speed"];        
            this.backgroundClass = settings["backgroundClass"];
            this.colorClass = settings["colorClass"];
            this.fontSize = settings["fontSize"];
        }
        this.updateFont();
    },
    ready() {
        window.addEventListener('scroll', this.scorll);
    },
    watch: {
        'currentChapter': 'getBookChapterContent',
    },
    methods: {
        //回到上次位置
        returnPos() {
            console.log("returnPos");
            let readRecord = JSON.parse(window.localStorage.getItem('followBookList'));
            if (readRecord[this.$route.params.bookId]) {
                this.currentChapter = parseInt(readRecord[this.$route.params.bookId].chapter);
                document.getElementById("container").scrollTop = readRecord[this.$route.params.bookId].readPos;
            }
        },
        returnTop() {
            let readRecord = JSON.parse(window.localStorage.getItem('followBookList'));
            document.getElementById("container").scrollTop = 0;
        },
        settings() {
            this.setting = !this.setting;
        },
        // todo 暂时获取一个章节内容，后续需要缓存3个章节左右
        getBookChapterContent() {
            this.loading = true;
            api.getBookChapterContent(this.loadedChapters[parseInt(this.currentChapter)].link).then(response => {
                this.title = response.data.title
                this.bookChaptersContent = response.data.chapter;
                this.loading = false;
                setTimeout(this.updateFont, 100);
            }).catch(err => {
                this.$Message.error('获取章节失败！');
                console.log(err);
            });
            this.updateFont();
        },
        operationAction($event) {
            //判断点击位置 执行不同操作
            console.log("in")
            let el = $event.pointers[0] || $event.srcEvent;
            if (this.isShowChapter) {
                this.isShowChapter = false;
                return;
            }
            let screenHeight = document.body.clientHeight;
            let gap = document.body.clientHeight / 3;
            let targetPos = el.clientY;
            let contanierEle = document.getElementById('container');
            if (0 < targetPos && targetPos < gap) {
                this.operation = false;
                this.setting = false;
                contanierEle.scrollTop -= screenHeight;
            }
            if (targetPos > gap && targetPos < screenHeight - gap) {
                this.operation = !this.operation;
                this.setting = false;
            }
            if (screenHeight - gap < targetPos && targetPos < screenHeight) {
                this.operation = false;
                this.setting = false;
                //判断是否到底部
                if (contanierEle.scrollHeight === contanierEle.scrollTop + screenHeight || contanierEle.scrollHeight < contanierEle.scrollTop + screenHeight) {
                    if (this.currentChapter >= this.bookChapter.chapters.length-1) {
                        this.$Message.info('这已经是最新的章节了~');
                        return;
                    } else {
                        //当前章节加1
                        this.currentChapter = parseInt(this.currentChapter) + 1;
                        if (this.loadedChapters[this.currentChapter].click == 0)
                            this.currentChapter = parseInt(this.currentChapter) + 1;
                    }
                }
                contanierEle.scrollTop += screenHeight;
            }
        },
        //切换日间/夜间模式
        changeMode() {
            this.nightMode = !this.nightMode;
            if (!this.nightMode) {
                this.backgroundClass = "";
                this.colorClass = "";
            } else {
                this.backgroundClass = "background-0";
                this.colorClass = "color-0";
            }
        },
        //显示目录
        showChapter() {
            this.isShowChapter = true;
        },
        //点击目录，跳转章节
        jumpChapter(index) {
            this.currentChapter = index;
            this.isShowChapter = false;
            this.operation = true;
        },
        //记录阅读历史
        recordReadHis(readRecord) {
            //目录正反序时，记录的都是正序排列的实际索引
            console.log(this.currentChapter);
            let chapterRecord = this.chapterDescSort ? this.bookChapter.chapters.length - this.currentChapter - 1 : this.currentChapter;
            readRecord[this.$route.params.bookId] = {
                cover: this.$store.state.bookInfo.cover,
                title: this.$store.state.bookInfo.title,
                chapter: chapterRecord,
                readPos: document.getElementById('container').scrollTop
            }
            window.localStorage.setItem('followBookList', JSON.stringify(readRecord));
        },
        //添加小说到书架
        addBook() {
            let readRecord = JSON.parse(window.localStorage.getItem('followBookList')) || {};
            this.recordReadHis(readRecord);
            this.$Message.success('添加成功！');
            this.$router.push('/book/' + this.bookChapter.book);
        },
        //不添加小说到书架
        dontAddBookToShelf() {
            this.dontAddBook = true;
            this.$router.push('/book/' + this.bookChapter.book);
        },
        //章节倒叙查看
        descSort() {
            this.chapterDescSort = !this.chapterDescSort;
            this.bookChapter.chapters.reverse();
            this.loadedChapters = this.bookChapter.chapters;
            this.loadPages = 1;
        },
        //滚动加载到底部，显示更多
        onScroll: function (e, position) {
            //if (position.scrollTop > 1300 * this.loadPages) {
            //    this.loadedChapters = this.loadedChapters.concat(this.bookChapter.chapters.slice(50 * this.loadPages, 50 * this.loadPages + 50));
            //   this.loadPages++;
            //    console.log("onScroll");
            //}
        },
        updateFont() {
            var fontSize = this.fontSize;
            var fontFamily = this.fontFamily;
            this.fontFamily = "KaiTi";
            Array.prototype.slice.call(document.getElementsByTagName("span")).forEach(function (ele) {
                    ele.style.fontSize = fontSize + 'rem';
                    ele.style.lineHeight = fontSize + 0.4 + 'rem';
                    ele.style.fontFamily = fontFamily;
                });
            Array.prototype.slice.call(document.getElementsByTagName("img")).forEach(function (ele) {
                    ele.style.maxWidth =  '90vw';
                    ele.style.maxHeight = '100vh';
                    ele.style.width = "auto";
                    ele.style.height = "auto";
                });
        },
        add_fontsize(a) {
            console.log(a);
            var fontSize = this.fontSize;
            var fontFamily = this.fontFamily;
            if (a == 0) {
                fontSize = 1.5;
                Array.prototype.slice.call(document.getElementsByTagName("span")).forEach(function (ele) {
                        ele.style.fontSize = fontSize + 'rem';
                        ele.style.lineHeight = fontSize  + 0.4 + 'rem';
                        ele.style.fontFamily = fontFamily;
                });
            } else if (a == 1 && fontSize < 2.5) {
                fontSize += 0.1;
                Array.prototype.slice.call(document.getElementsByTagName("span")).forEach(function (ele) {
                        ele.style.fontSize = fontSize + 'rem';
                        ele.style.lineHeight = fontSize + 0.4 + 'rem';
                        ele.style.fontFamily = fontFamily;
                });
            } else if (a == -1 && fontSize > 1.0) {
                fontSize -= 0.1;
                Array.prototype.slice.call(document.getElementsByTagName("span")).forEach(function (ele) {
                        ele.style.fontSize = fontSize + 'rem';
                        ele.style.lineHeight = fontSize + 0.4 + 'rem';
                        ele.style.fontFamily = fontFamily;
                });
            } else if (a == 2 ) {
                Array.prototype.slice.call(document.getElementsByTagName("span")).forEach(function (ele) {
                        ele.style.fontSize = fontSize + 'rem';
                        ele.style.lineHeight = fontSize + 0.4 + 'rem';
                        ele.style.fontFamily = fontFamily;
                });
            } else {
                this.$Message.info('不能再继续改变字体了');
            }
            this.fontSize = fontSize;
        },
        change_back(a) {
            this.backgroundClass = "background-" + a;
        },
        change_color(a) {
            this.colorClass = "color-" + a;
        },
        dbclickEvent() {
            var speed = this.speed;
            if (!this.dbflag) {
                clearInterval(this.timer);
                this.timer=self.setInterval(function() {
                    var currentpos;
                    currentpos=document.getElementById("container").scrollTop;
                    document.getElementById("container").scrollTop = currentpos+speed;
                },100);
                this.dbflag = true;
                this.autoread = false;
                this.$Message.info('开始自动翻页');
            } else {
                clearInterval(this.timer);
                this.timer = Object();
                this.$Message.info('自动翻页取消');
                this.autoread = false;
                this.dbflag = false;
            }
        },
        add_speed(a) {
            if (a == 1) {
                this.speed += 1;
                this.$Message.info('增加成功');
            } else if (a == -1) {
                this.speed -= 1;
                if(this.speed == 0)
                    this.$Message.info('继续减少可以反向预览');
                else
                    this.$Message.info('减少成功');
            }
        },
        update_family(a) {
            this.fontFamily = a;
        },
        auto_read() {
            var speed = this.speed;
            if (this.dbflag || this.autoread) {
                clearInterval(this.timer);
                this.timer = Object();
                this.dbflag = false;
                this.autoread = false;
                this.$Message.info('自动翻页取消');
            } else if (!this.autoread) {
                clearInterval(this.timer);
                this.dbflag = false;
                this.autoread = true;
                this.timer = self.setInterval(function() {
                    var currentpos;
                    currentpos=document.getElementById("container").scrollTop;
                    document.getElementById("container").scrollTop = currentpos+document.body.clientHeight;
                },5000 - speed*200)
                this.$Message.info('开始自动翻页');
            }
        },
        get_next() {
        }
    },
    beforeRouteEnter(to, from, next) {
        var str = to.path;
        next(vm => {
            vm.preView = from.fullPath;
            if (vm.preView == "/")
                vm.preView = "/bookshelf"
        });
    },
    beforeRouteLeave(to, from, next) {
        clearInterval(this.timer);
        let settings = {};
        settings["speed"] = this.speed;        
        settings["backgroundClass"] = this.backgroundClass;
        settings["colorClass"] = this.colorClass;
        settings["fontSize"] = this.fontSize;
        window.localStorage.setItem('settings', JSON.stringify(settings));
        this.dontAddBook && next();
        let readRecord = JSON.parse(window.localStorage.getItem('followBookList')) || {};
        if (!readRecord[this.bookChapter.book]) {
            this.recordReadHis(readRecord);
            this.showAddToShelf = true;
            next(true);
        } else {
            this.recordReadHis(readRecord);
            next();
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.container {
    background: #dad9d4;
    width: 100vw;
    height: 100vh;
    overflow: auto;
    color: #000;
    padding-left: 2vw;
    padding-right: 2vw;
}

header {
    text-align: center;
    padding-top: 1rem;
    margin-bottom: 1rem;
    font-size: 2rem;
    font-weight: bold;
}

article {
    font-size: 1.5rem;
    line-height: 1.9rem;
    padding: 1rem;
}

span {
    font-size: 1.5rem;
}

.head {
    position: fixed;
    top: 0;
    left: 0;
    height: 3rem;
    width: 100vw;
    background: #fff;
    color: #000000;
    text-align: center;
    line-height: 3rem;
}

.menu {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    position: fixed;
    bottom: 0;
    left: 0;
    color: #000;
    background: #fff;
    height: 3.5rem;
    width: 100vw;
}

.setting {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    position: fixed;
    bottom: 3.5rem;
    left: 0;
    background: #fff;
    height: 2.5rem;
    width: 100vw;
    border-top: 1px solid #C8C0A8;
    border-bottom: 1px solid #C8C0A8;
}
#autoread {
    margin-top: 0.5rem;
    flex-direction: row;
    vertical-align: middle;
    position: relative;
}


.setting2 {
    display: flex;
    justify-content: space-around;
    position: fixed;
    bottom: 6rem;
    left: 0;
    background: #fff;
    height: 3.5rem;
    width: 100vw;
}
.font-border {
    border: 1px solid #C8C0A8;
    border-radius: 10%;
    margin-top: 0.5rem;
    margin-bottom: 0.5rem;
}

.setting3 {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    position: fixed;
    bottom: 9.5rem;
    left: 0;
    background: #fff;
    height: 3.5rem;
    width: 100vw;
}
.setting4 {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    position: fixed;
    top: 9rem;
    left: 0;
    background: #000;
    height: 3.5rem;
    width: 100vw;
}
.circle {
    width: 2rem;
    height: 2rem;
    border-radius: 50%;
    -moz-border-radius: 50%;
    -webkit-border-radius: 50%;
    text-align: center;
    vertical-align: middle;
    font-size: 1.3rem;
    justify-content:center;
}

.menu-btn {
    display: flex;
    flex-direction: column;
    justify-content: center;
    color: #000;
    text-align: center;
    font-size: 0.7rem !important;
}

.menu-img {
    height: 2.3rem;
    width: auto;
}

.menu-btn i {
    font-size: 1.6rem !important;
}

.menu-btn span {
    font-size: 0.8rem !important;
}

.arrow-left {
    color: #005d9c;
    position: absolute;
    left: 1rem;
    line-height: 3rem;
    font-size: 1.5rem !important;
}

.night-mode {
    background: #383434;
    color: #807d7d;
}

.chapter-list {
    position: absolute;
    top: 0rem;
    left: 0;
    height: 100vh;
    overflow: auto;
    background: #fff;
    width: 80vw;
}

.title {
    font-size: 1rem;
    color: #000000;
}

.title2 {
    font-size: 0.8rem;
    color: #807d7d;
}

.chapter-list ul {
    margin-top: 2.5rem;
}

.chapter-list li {
    padding-top: 0.5rem;
    padding-left: 1rem;
    line-height: 2.5rem;
    border-bottom: 1px solid #f2f2f2;
}

.chapter-contents {
    top: 0;
    left: 0;
    width: 75vw;
    background: #fff;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    line-height: 2.5rem;
    padding-left: 1rem;
    color: #000;
}

.chapter-sort {
    margin-right: 2rem;
    font-size: 1.4rem !important;
}

.night-mode {
    background: #383434;
    color: #807d7d;
}

.background-0 {
    background: #383434;
}
.background-1 {
    background: #CCC9C1;
}
.background-2 {
    background: #C8C0A8;
}
.background-3 {
    background: #BCC6BD;
}
.background-4 {
    background: #FDEEC3;
}
.color-0 {
    background: #FEFBEB;
    color: #363636;
}
.color-back-0 {
    background: #FEFBEB;
    color: #363636;
}
.color-1 {
    background: #DEF0ED;
    color: #363636; 
}
.color-back-1 {
    background: #DEF0ED;
    color: #363636; 
}
.color-2 {
    background: #CEB294;
    color: #363636; 
}
.color-back-2 {
    background: #CEB294;
    color: #363636;   
}
.color-3 {
    background: #DED5C3;
    color: #363636; 
}
.color-back-3 {
    background: #DED5C3;
    color: #363636;   
}
.color-4 {
    background: #375149;
    color: #FDFBFC;
}
.color-back-4 {
    background: #375149;
    color: #FDFBFC;   
}
.selected {
    background: #66ccFF;
}
#fontStyle {
    font-family: STKaiti;
}
.mulucenter {
    text-align: center;
    color: #005d9c;
}
.chapter-list::-webkit-scrollbar {/*滚动条整体样式*/
    width: 1rem;     /*高宽分别对应横竖滚动条的尺寸*/
    height: 1rem;
}
.chapter-list::-webkit-scrollbar-thumb {/*滚动条里面小方块*/
    border-radius: 5px;
    -webkit-box-shadow: inset 0 0 5px rgba(0,0,0,0.2);
    background: rgba(0,0,0,0.2);
}
.chapter-list::-webkit-scrollbar-track {/*滚动条里面轨道*/
    -webkit-box-shadow: inset 0 0 5px rgba(0,0,0,0.2);
    border-radius: 0;
    background: rgba(0,0,0,0.1);
}
</style>
