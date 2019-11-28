<template>
    <div class="index-box">
        <el-container>
            <el-main style="padding: 0!important;">
                <el-header>
                    <Header></Header>
                </el-header>
                <!--分类-->
                <el-row :span="24" style="width: 1210px;margin: 0 auto 30px;display: flex;justify-content: space-around;flex-wrap: wrap">
                    <div class="zfx-box" @click="pushs">
                        <div class="war-box">
                            <span class="el-icon-arrow-right"></span>
                            <div class="ho-box">
                                <img src="https://cs.vmovier.com/Uploads/cover/2019-11-14/5dcd24d219390_cut.jpeg@600w_400h_1e_1c.jpg" alt="">
                                <span class="name-box">#动作#</span>
                            </div>
                        </div>
                    </div>
                    <div class="zfx-box" @click="pushs1">
                        <div class="war-box">
                            <span class="el-icon-arrow-right"></span>
                            <div class="ho-box">
                                <img src="https://cs.vmovier.com/Uploads/Series/2017-07-07/595ef6c7b9b25.jpg" alt="">
                                <span class="name-box">#战争#</span>
                            </div>
                        </div>
                    </div>
                    <div class="zfx-box" @click="pushs2">
                        <div class="war-box">
                            <span class="el-icon-arrow-right"></span>
                            <div class="ho-box">
                                <img src="https://cs.vmovier.com/Uploads/Series/2017-07-07/595ef6992fd6e.jpg" alt="">
                                <span class="name-box">#科幻#</span>
                            </div>
                        </div>
                    </div>
                    <div class="zfx-box" @click="pushs3">
                        <div class="war-box">
                            <span class="el-icon-arrow-right"></span>
                            <div class="ho-box">
                                <img src="https://cs.vmovier.com/Uploads/cover/2018-03-15/5aaa34100b019_cut.jpeg@600w_400h_1e_1c.jpg" alt="">
                                <span class="name-box">#悬疑#</span>
                            </div>
                        </div>
                    </div>
                    <div class="zfx-box" @click="pushs4">
                        <div class="war-box">
                            <span class="el-icon-arrow-right"></span>
                            <div class="ho-box">
                                <img src="https://cs.vmovier.com/Uploads/Series/2017-07-07/595ef5807352a.jpg" alt="">
                                <span class="name-box">#喜剧#</span>
                            </div>
                        </div>
                    </div>
                    <div class="zfx-box" @click="pushs5">
                        <div class="war-box">
                            <span class="el-icon-arrow-right"></span>
                            <div class="ho-box">
                                <img src="https://cs.vmovier.com/Uploads/Series/2017-07-07/595ef609815e3.jpg" alt="">
                                <span class="name-box">#爱情#</span>
                            </div>
                        </div>
                    </div>
                    <div class="zfx-box" @click="pushs6">
                        <div class="war-box">
                            <span class="el-icon-arrow-right"></span>
                            <div class="ho-box">
                                <img src="https://cs.vmovier.com/Uploads/Series/2017-07-07/595ef63d2134e.jpg" alt="">
                                <span class="name-box">#剧情#</span>
                            </div>
                        </div>
                    </div>
                    <div class="zfx-box" @click="pushs7">
                        <div class="war-box">
                            <span class="el-icon-arrow-right"></span>
                            <div class="ho-box">
                                <img src="https://cs.vmovier.com/Uploads/Series/2017-07-07/595ef668bc201.jpg" alt="">
                                <span class="name-box">#动画#</span>
                            </div>
                        </div>
                    </div>
                    <div class="zfx-box" @click="pushs8">
                        <div class="war-box">
                            <span class="el-icon-arrow-right"></span>
                            <div class="ho-box">
                                <img src="https://cs.vmovier.com/Uploads/cover/2019-11-19/5dd3abf7d2050_cut.jpeg@600w_400h_1e_1c.jpg" alt="">
                                <span class="name-box">#惊悚#</span>
                            </div>
                        </div>
                    </div>
                    <div class="zfx-box" @click="pushs9">
                        <div class="war-box">
                            <span class="el-icon-arrow-right"></span>
                            <div class="ho-box">
                                <img src="https://cs.vmovier.com/Uploads/cover/2014-05-16/5375dfd36507b_cut.jpeg@600w_400h_1e_1c.jpg" alt="">
                                <span class="name-box">#犯罪#</span>
                            </div>
                        </div>
                    </div>
                    <div class="zfx-box" @click="pushss">
                        <div class="war-box">
                            <span class="el-icon-arrow-right"></span>
                            <div class="ho-box">
                                <img src="https://cs.vmovier.com/Uploads/Series/2017-07-07/595ef6b89cebb.jpg" alt="">
                                <span class="name-box">#传记#</span>
                            </div>
                        </div>
                    </div>
                    <div class="zfx-box"></div>
                </el-row>
                <el-footer>
                    <el-row :span="24" style="font-size: 12px">
                        <span style="margin-right: 20px">Copyright © 2011-2018</span>
                        <span style="margin-right: 20px">
                            <a href="/" style="text-decoration: none;color: #cccccc">爱电影</a>
                        </span>
                        <span style="margin-right: 10px">京ICP备14003808号-5</span>
                        <span class="tu-box">
                            <img src="../../assets/ba-icon.png" alt="">
                            <span>京公网安备11010102002904号</span>
                        </span>
                    </el-row>
                </el-footer>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    // @ is an alias to /src
    // import HelloWorld from '@/components/HelloWorld.vue'
    import Header from '@/components/header/header.vue'

    export default {
        name: 'index',
        components: {
            // HelloWorld
            Header
        },
        data(){
            return {
                activeIndex:'1',
                mySqlData:[],
            }
        },
        methods: {
            handleSelect() {
            },
            pushs(){
                this.$router.push("/middle/action")
            },
            pushs1(){
                this.$router.push("/middle/war")
            },
            pushs2(){
                this.$router.push("/middle/science")
            },
            pushs3(){
                this.$router.push("/middle/suspense")
            },
            pushs4(){
                this.$router.push("/middle/comedy")
            },
            pushs5(){
                this.$router.push("/middle/love")
            },
            pushs6(){
                this.$router.push("/middle/inspiration")
            },
            pushs7(){
                this.$router.push("/middle/animation")
            },
            pushs8(){
                this.$router.push("/middle/thriller")
            },
            pushs9(){
                this.$router.push("/middle/crime")
            },
            pushss(){
                this.$router.push("/middle/record")
            },
        }
    }
</script>
<style scoped>
    .index-box{
        width: 100%;
        height: 100%;
    }
    .el-container{
        width: 100%;
        height: 100%;
        /*background: #555;*/
    }
    .el-header{
        background-color: rgb(249, 249, 249);
        box-shadow: rgba(0, 0, 0, 0.1) 0px 1px 4px;
        opacity: 0.97;
        color: #333;
        text-align: center;
        line-height: 60px;
        padding: 0 24px!important;
        /*position: fixed;*/
        z-index: 10;
        width: 100%;
    }
    .el-main {
        background-color: #F1F1F1;
        color: #333;
        text-align: center;
        /*line-height: 160px;*/
        /*padding: 0 24px!important;*/
    }
    .left-box{
        font-weight: 600;
        font-size: 24px;
    }
    .el-footer {
        background-color: #222222;
        color: #cccccc;
        text-align: center;
        line-height: 60px;
        height: 60px!important;
    }
    .zfx-box{
        width: 272px;
        height: 182px;
        margin: 30px 0 0 30px;
    }
    .war-box{
        width: 100%;
        height: 100%;
        background: #3498DB;
        position: relative;
        cursor: pointer;
        overflow: hidden;
        display: block;
    }
    .war-box span{
        position: absolute;
        right: 10px;
        top: 0;
        bottom: 0;
        margin: auto 0;
        font-size: 26px;
        color: white;
        line-height: 182px;
        text-align: center;
    }
    .war-box img{
        width: 100%;
        height: 100%;
        z-index: 10;
        position: absolute;
        top: 0;
        left: 0;
    }
    .ho-box{
        width: 100%;
        height: 100%;
        position: absolute;
        transition: all ease .4s;
    }
    .war-box:hover .ho-box{
        transform: translateX(-40px);
    }
    .name-box{
        position: absolute;
        z-index: 20;
        left: 0;
        top: 0;
        right: 0;
        bottom: 0;
        margin: auto;
    }
</style>
