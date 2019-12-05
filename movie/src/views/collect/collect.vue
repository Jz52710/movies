<template>
    <div class="index-box">
        <el-container>
            <el-main style="padding: 0!important;">
                <el-header>
                    <Header></Header>
                </el-header>
                <!--分类-->
                <div class="intelligent-box">
                    <el-container class="container-box">
                        <el-col :span="24" class="zhi-box" style="width: 870px;margin: 0 auto">
                            <el-col :span="24" class="zhong-box">
                                <el-col :span="8" class="hb-box" v-for="(item,index) in mySqlData" :key="index">
                                    <el-row :span="24">
                                        <el-col :span="4" class="img-box">
                                            <a :href="item.official">
                                                <img :src="getImages(item.img)" alt="123">
                                            </a>
                                        </el-col>
                                        <el-col :span="18" style="padding: 5px;margin: 34px 0">
                                            <el-row :span="24" style="margin-bottom: 6px">
                                                <a :href="item.details">
                                                    <el-col :span="14" class="name-box" v-text="item.mname" style="white-space: nowrap;overflow: hidden;text-overflow: ellipsis;position: static!important;"></el-col>
                                                </a>
                                                <el-col :span="6" class="year-box" v-text="item.years"></el-col>
                                                <div @click="dels(item.mid)">
                                                    <el-col :span="2" class="year-box el-icon-star-off yr-box" style="text-align: right;cursor: pointer">想看</el-col>
                                                </div>
                                            </el-row>
                                            <el-row :span="24" style="margin-bottom: 6px">
                                                <el-col class="db-box">
                                                    <a :href="item.details">豆瓣
                                                        <span>{{ item.score}}</span>
                                                    </a>
                                                </el-col>
                                            </el-row>
                                            <el-row :span="24" style="margin-bottom: 6px">
                                                <el-col class="dyy-box">
                                                    <span class="dy-box">语言：</span>
                                                    <span class="dyname-box" v-text="item.languages"></span>
                                                </el-col>
                                            </el-row>
                                            <el-row :span="24" style="margin-bottom: 6px">
                                                <el-col class="dyy-box">
                                                    <span class="dy-box">导演：</span>
                                                    <span class="dyname-box" v-text="item.director"></span>
                                                </el-col>
                                            </el-row>
                                            <el-row :span="24" style="margin-bottom: 6px">
                                                <el-col class="dyy-box">
                                                    <span class="dy-box">类型：</span>
                                                    <span class="dyname-box" v-text="item.mold"></span>
                                                </el-col>
                                            </el-row>
                                            <el-row :span="24" style="margin-bottom: 6px;width: 400px!important;display: flex">
                                                <el-col class="dyy-box" style="width: 400px!important;">
                                                    <el-col :span="3" style="width: 42px!important;">
                                                        <span class="dy-box">主演：</span>
                                                    </el-col>
                                                    <el-col :span="20" style="white-space: nowrap;overflow: hidden;text-overflow: ellipsis;">
                                                        <span class="dyname-box" v-text="item.act" style="width: 400px!important;"></span>
                                                    </el-col>
                                                </el-col>
                                            </el-row>
                                        </el-col>
                                    </el-row>
                                </el-col>
                            </el-col>
                        </el-col>
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
                    </el-container>

                </div>

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
            getImages( _url ){
                if( _url !== undefined ){
                    let _u = _url.substring( 7 );
                    return 'https://images.weserv.nl/?url=' + _u;
                }
            },
            dels(val){
                let res = {'mid':val};
                this.$axios.delete('/api/collection',{data:res}).then(()=>{
                    this.$message.error('已移除想看');
                }).catch(function (error) {
                    alert(error)
                });
            },
        },
        mounted(){
            this.$axios.get('/api/collection').then((data)=>{
                // alert(data.data.data[0].score);
                this.mySqlData = data.data.data
            }).catch((error)=>{
                alert(error)
            })
        },
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
    .intelligent-box{
        width: 100%;
        height: 100%;
        margin:0 auto;
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
        margin-top: 10px;
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
    .yr-box:hover{
        color: #FF9900;
    }
</style>
