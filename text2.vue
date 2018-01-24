一：空span如何换行（不用nbsp因为会错位）

二：进度条 ！

三：历史记录显示 or 上次阅读时间（BOOK BOOKSHELF 作者下面） ！

四：章节定位目前章节（CHAPTER LIST） ！

五：搜索时底框

            <!--div class = "middle">
            .progress {
    height: 10px;
    width: 90%;
    margin-bottom: 10px;
    float: left;
    overflow: hidden;
    background: #f5f5f5;
    border-radius: 4px;
    -webkit-box-shadow: inset 0 1px 2px rgba(0,0,0,.1);
    box-shadow: inset 0 1px 2px rgba(0,0,0,0.1);
}
.progress-bar {
    width: 0;
    height: 100%;
    font-size: 12px;
    line-height: 20px;
    color: #66ccff;
    text-align: center;
    background-color: #337ab7;
    border-radius: 4px;
    -webkit-box-shadow: inset 0 -1px 0 rgba(0,0,0,.1);
    box-shadow: inset 0 -1px 0 rgba(0,0,0,0.1);
    -webkit-transition: width .6s ease;
    -o-transition: width .6s ease;
}
.progress.active .progress-bar {
    -webkit-animation: progress-bar-stripes 2s linear infinite;
    -o-animation: progress-bar-stripes 2s linear infinite;
    animation: progress-bar-stripes 2s linear infinite;
}
@keyframes progress-bar-stripes {
    0% {
        background-position: 40px 0;
    }
    100% {
        background-position: 0 0;
    }
}
.progress-bar-info {
    background-color: #5bc0de;
}
.progress-striped .progress-bar {
    background-size: 40px 40px;
    background-image: -webkit-linear-gradient(45deg,rgba(255,255,255,.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,.15) %50, rgba(255,255,255,.15) 75%, transparent 75%, transparent);
    background-image: -o-linear-gradient(45deg,rgba(255,255,255,.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,.15) %50, rgba(255,255,255,.15) 75%, transparent 75%, transparent);
    background-image: linear-gradient(45deg,rgba(255,255,255,.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,.15) %50, rgba(255,255,255,.15) 75%, transparent 75%, transparent);
}
            &nbsp;
            </div>
            <div class="move-circle">
                &nbsp;
            <v-touch @swipeleft="get_next" @swiperight="get_next">swipeleft</v-touch> 
            <div id="progressbar"></div>
            <div class="progress-outer">
                <div class="progress" :class="{'progress-striped active': true}">
                    <div class="progress-bar"
                        :class="type && 'progress-bar-' + type"
                        role="progressbar"
                        :style="{width: (percent < 100 ? percent : 100) + '%'}">
                        
                    </div>
                </div>
            </div>
            </div-->