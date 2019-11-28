<template>
    <div class="intelligent-box">
        <el-container class="container-box">
            <el-col :span="24" class="zhi-box">
                <el-col :span="24" class="zhong-box">
                    <el-col :span="8" class="hb-box" v-for="(item,index) in mysqlData" :key="index">
                        <el-row :span="24">
                            <el-col :span="4" class="img-box">
                                <a :href="item.official">
                                    <img :src="getImages(item.img)" alt="123">
                                </a>
                            </el-col>
                            <el-col :span="18" style="padding: 5px;margin: 34px 0">
                                <el-row :span="24" style="margin-bottom: 6px">
                                    <a :href="item.details">
                                    <el-col :span="14" class="name-box" v-text="item.mname" style="white-space: nowrap;overflow: hidden;text-overflow: ellipsis;"></el-col>
                                        </a>
                                    <el-col :span="8" class="year-box" v-text="item.years"></el-col>
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
        </el-container>

    </div>
</template>

<script>
    // @ is an alias to /src
    // import HelloWorld from '@/components/HelloWorld.vue'

    export default {
        name: 'intelligent',
        // props:['mysqlData','total','currentPage','pageSize'],
        components: {
            // HelloWorld
        },
        data(){
            return {
                activeIndex: '1',
                total:200,
                currentPage:1,
                pageSize:10,
                // src:'http://dianying.fm/media/poster/213/2131459.jpg',
                // url: 'http://movie.douban.com/subject/2131459/',
                value:9.3,
                mysqlData:[],
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
            handleSizeChange() {

            },
            handleCurrentChange(val){
                this.$emit("currentPage",val)
                // alert(val)
                // this.currentPage = val;
            },
        },
        mounted(){
            let data = {mold:'剧情'};
            this.$axios.post('/api/sess',data).then((data)=>{
                // alert(data.data.data[0].score);
                this.mysqlData = data.data.data
            }).catch((error)=>{
                alert(error)
            })
        },
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
</style>
