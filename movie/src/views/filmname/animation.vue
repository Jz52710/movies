<template>
    <div class="classify-box">
        <el-row :span="24" type="flex" justify="space-around" style="flex-wrap: wrap;padding-top: 15px">
            <el-col :span="8" class="hb-box">
                        <el-row :span="24">
                            <el-col :span="4" class="img-box">
                                <a href="">
                                    <img :src="src" alt="">
                                </a>
                            </el-col>
                            <el-col :span="18" style="padding: 5px;margin: 24px 0">
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col :span="14" class="name-box">千与千寻</el-col>
                                    <el-col :span="8" class="year-box">2001</el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="db-box">
                                        <el-rate
                                                v-model="value"
                                                disabled
                                                show-score
                                                text-color="#ff9900"
                                                score-template="{value}"
                                                :max="10"
                                        style="margin-bottom: 6px">
                                        </el-rate>
                                        <a :href="url">豆瓣
                                            <span>9.3</span>
                                        </a>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">语言：</span>
                                        <span class="dyname-box">英语</span>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">导演：</span>
                                        <span class="dyname-box">宫崎骏</span>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">类型：</span>
                                        <span class="dyname-box">剧情 / 动画 / 奇幻</span>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">主演：</span>
                                        <span class="dyname-box">柊瑠美 / 入野自由 / 夏木真理 / 菅原文太...</span>
                                    </el-col>
                                </el-row>
                            </el-col>
                        </el-row>
                    </el-col>
            <el-col :span="8" class="hb-box">
                        <el-row :span="24">
                            <el-col :span="4" class="img-box">
                                <a href="">
                                    <img :src="src" alt="">
                                </a>
                            </el-col>
                            <el-col :span="18" style="padding: 5px;margin: 24px 0">
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col :span="14" class="name-box">千与千寻</el-col>
                                    <el-col :span="8" class="year-box">2001</el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="db-box">
                                        <el-rate
                                                v-model="value"
                                                disabled
                                                show-score
                                                text-color="#ff9900"
                                                score-template="{value}"
                                                :max="10"
                                        style="margin-bottom: 6px">
                                        </el-rate>
                                        <a :href="url">豆瓣
                                            <span>9.3</span>
                                        </a>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">语言：</span>
                                        <span class="dyname-box">英语</span>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">导演：</span>
                                        <span class="dyname-box">宫崎骏</span>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">类型：</span>
                                        <span class="dyname-box">剧情 / 动画 / 奇幻</span>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">主演：</span>
                                        <span class="dyname-box">柊瑠美 / 入野自由 / 夏木真理 / 菅原文太...</span>
                                    </el-col>
                                </el-row>
                            </el-col>
                        </el-row>
                    </el-col>
            <el-col :span="8" class="hb-box">
                        <el-row :span="24">
                            <el-col :span="4" class="img-box">
                                <a href="">
                                    <img :src="src" alt="">
                                </a>
                            </el-col>
                            <el-col :span="18" style="padding: 5px;margin: 24px 0">
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col :span="14" class="name-box">千与千寻</el-col>
                                    <el-col :span="8" class="year-box">2001</el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="db-box">
                                        <el-rate
                                                v-model="value"
                                                disabled
                                                show-score
                                                text-color="#ff9900"
                                                score-template="{value}"
                                                :max="10"
                                        style="margin-bottom: 6px">
                                        </el-rate>
                                        <a :href="url">豆瓣
                                            <span>9.3</span>
                                        </a>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">语言：</span>
                                        <span class="dyname-box">英语</span>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">导演：</span>
                                        <span class="dyname-box">宫崎骏</span>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">类型：</span>
                                        <span class="dyname-box">剧情 / 动画 / 奇幻</span>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">主演：</span>
                                        <span class="dyname-box">柊瑠美 / 入野自由 / 夏木真理 / 菅原文太...</span>
                                    </el-col>
                                </el-row>
                            </el-col>
                        </el-row>
                    </el-col>
            <el-col :span="8" class="hb-box">
                        <el-row :span="24">
                            <el-col :span="4" class="img-box">
                                <a href="">
                                    <img :src="src" alt="">
                                </a>
                            </el-col>
                            <el-col :span="18" style="padding: 5px;margin: 24px 0">
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col :span="14" class="name-box">千与千寻</el-col>
                                    <el-col :span="8" class="year-box">2001</el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="db-box">
                                        <el-rate
                                                v-model="value"
                                                disabled
                                                show-score
                                                text-color="#ff9900"
                                                score-template="{value}"
                                                :max="10"
                                        style="margin-bottom: 6px">
                                        </el-rate>
                                        <a :href="url">豆瓣
                                            <span>9.3</span>
                                        </a>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">语言：</span>
                                        <span class="dyname-box">英语</span>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">导演：</span>
                                        <span class="dyname-box">宫崎骏</span>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">类型：</span>
                                        <span class="dyname-box">剧情 / 动画 / 奇幻</span>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">主演：</span>
                                        <span class="dyname-box">柊瑠美 / 入野自由 / 夏木真理 / 菅原文太...</span>
                                    </el-col>
                                </el-row>
                            </el-col>
                        </el-row>
                    </el-col>
            <el-col :span="8" class="hb-box">
                        <el-row :span="24">
                            <el-col :span="4" class="img-box">
                                <a href="">
                                    <img :src="src" alt="">
                                </a>
                            </el-col>
                            <el-col :span="18" style="padding: 5px;margin: 24px 0">
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col :span="14" class="name-box">千与千寻</el-col>
                                    <el-col :span="8" class="year-box">2001</el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="db-box">
                                        <el-rate
                                                v-model="value"
                                                disabled
                                                show-score
                                                text-color="#ff9900"
                                                score-template="{value}"
                                                :max="10"
                                        style="margin-bottom: 6px">
                                        </el-rate>
                                        <a :href="url">豆瓣
                                            <span>9.3</span>
                                        </a>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">语言：</span>
                                        <span class="dyname-box">英语</span>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">导演：</span>
                                        <span class="dyname-box">宫崎骏</span>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">类型：</span>
                                        <span class="dyname-box">剧情 / 动画 / 奇幻</span>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">主演：</span>
                                        <span class="dyname-box">柊瑠美 / 入野自由 / 夏木真理 / 菅原文太...</span>
                                    </el-col>
                                </el-row>
                            </el-col>
                        </el-row>
                    </el-col>
            <el-col :span="8" class="hb-box">
                        <el-row :span="24">
                            <el-col :span="4" class="img-box">
                                <a href="">
                                    <img :src="src" alt="">
                                </a>
                            </el-col>
                            <el-col :span="18" style="padding: 5px;margin: 24px 0">
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col :span="14" class="name-box">千与千寻</el-col>
                                    <el-col :span="8" class="year-box">2001</el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="db-box">
                                        <el-rate
                                                v-model="value"
                                                disabled
                                                show-score
                                                text-color="#ff9900"
                                                score-template="{value}"
                                                :max="10"
                                        style="margin-bottom: 6px">
                                        </el-rate>
                                        <a :href="url">豆瓣
                                            <span>9.3</span>
                                        </a>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">语言：</span>
                                        <span class="dyname-box">英语</span>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">导演：</span>
                                        <span class="dyname-box">宫崎骏</span>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">类型：</span>
                                        <span class="dyname-box">剧情 / 动画 / 奇幻</span>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">主演：</span>
                                        <span class="dyname-box">柊瑠美 / 入野自由 / 夏木真理 / 菅原文太...</span>
                                    </el-col>
                                </el-row>
                            </el-col>
                        </el-row>
                    </el-col>
            <el-col :span="8" class="hb-box">
                        <el-row :span="24">
                            <el-col :span="4" class="img-box">
                                <a href="">
                                    <img :src="src" alt="">
                                </a>
                            </el-col>
                            <el-col :span="18" style="padding: 5px;margin: 24px 0">
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col :span="14" class="name-box">千与千寻</el-col>
                                    <el-col :span="8" class="year-box">2001</el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="db-box">
                                        <el-rate
                                                v-model="value"
                                                disabled
                                                show-score
                                                text-color="#ff9900"
                                                score-template="{value}"
                                                :max="10"
                                        style="margin-bottom: 6px">
                                        </el-rate>
                                        <a :href="url">豆瓣
                                            <span>9.3</span>
                                        </a>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">语言：</span>
                                        <span class="dyname-box">英语</span>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">导演：</span>
                                        <span class="dyname-box">宫崎骏</span>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">类型：</span>
                                        <span class="dyname-box">剧情 / 动画 / 奇幻</span>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">主演：</span>
                                        <span class="dyname-box">柊瑠美 / 入野自由 / 夏木真理 / 菅原文太...</span>
                                    </el-col>
                                </el-row>
                            </el-col>
                        </el-row>
                    </el-col>
            <el-col :span="8" class="hb-box">
                        <el-row :span="24">
                            <el-col :span="4" class="img-box">
                                <a href="">
                                    <img :src="src" alt="">
                                </a>
                            </el-col>
                            <el-col :span="18" style="padding: 5px;margin: 24px 0">
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col :span="14" class="name-box">千与千寻</el-col>
                                    <el-col :span="8" class="year-box">2001</el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="db-box">
                                        <el-rate
                                                v-model="value"
                                                disabled
                                                show-score
                                                text-color="#ff9900"
                                                score-template="{value}"
                                                :max="10"
                                        style="margin-bottom: 6px">
                                        </el-rate>
                                        <a :href="url">豆瓣
                                            <span>9.3</span>
                                        </a>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">语言：</span>
                                        <span class="dyname-box">英语</span>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">导演：</span>
                                        <span class="dyname-box">宫崎骏</span>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">类型：</span>
                                        <span class="dyname-box">剧情 / 动画 / 奇幻</span>
                                    </el-col>
                                </el-row>
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <el-col class="dyy-box">
                                        <span class="dy-box">主演：</span>
                                        <span class="dyname-box">柊瑠美 / 入野自由 / 夏木真理 / 菅原文太...</span>
                                    </el-col>
                                </el-row>
                            </el-col>
                        </el-row>
                    </el-col>
        </el-row>
    </div>
</template>

<script>
    // @ is an alias to /src
    // import HelloWorld from '@/components/HelloWorld.vue'

    export default {
        name: 'classify',
        components: {
            // HelloWorld
        },
        data(){
            return {
                src:'http://dianying.fm/media/poster/129/1291561.jpg',
                url:'http://movie.douban.com/subject/1291561/',
                value:9.3,
            }
        },
        methods: {

        }
    }
</script>
<style scoped>
    .intelligent-box{
        width: 100%;
        height: 100%;
    }
    .container-box{
        /*width: 100%;*/
        /*height: auto;*/
        /*background: #555;*/
    }
    /*.zhi-box{*/
    /*    margin: 0 auto;*/
    /*    display: flex;*/
    /*    justify-content: space-around;*/
    /*    flex-wrap: wrap;*/
    /*}*/
    .zhong-box{
        background: #f8f8f8;
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        padding-top: 15px;
    }
    .hb-box{
        width: 100%;
        border: 1px solid #ddd;
        background: white;
        margin-bottom: 30px;
    }
    .img-box{
        height: 246px;
        /*width: 100px;*/
        padding: 25px 0;
        margin: 0 25px;
    }
    .img-box a img{
        height: 196px;
        width: 100%;
    }
    .name-box{
        color: #337ab7;
        font-size: 26px;
        text-align: left;
    }
    .year-box{
        margin-top: 16px;
        font-size: 16px;
        text-align: left;
        color: #888888;
    }
    .db-box{
        text-align: left;
    }
    .db-box a{
        color: #00AB00;
        font-size: 14px;
        text-decoration: none;
    }
    .dyy-box{
        font-size: 14px;
        text-align: left;
    }
    .dy-box{
        font-weight: bold;
        color: #666666;
    }
    .dyname-box{
        color: #888888;
    }

</style>
