<template>
    <div class="header-box">
        <el-row :span="24">
            <el-col :span="4" class="left-box">
                iMovies
            </el-col>
            <el-col :span="20" class="right-box">
                <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" background-color="#F9F9F9" active-text-color="#409EFF" style="display:flex;">
                    <el-menu-item index="1">
                        <router-link :to="{name:'index'}" tag="div" style="width: 96px;">
                            首页
                        </router-link>
                    </el-menu-item>
                    <el-menu-item index="2">
                        <router-link :to="{name:'channel'}" tag="div" style="width: 96px;">
                            频道
                        </router-link>
                    </el-menu-item>
                </el-menu>
                <el-col :span="8" style="display: flex">
                    <!--搜索-->
                    <el-col :span="12">
                        <el-input placeholder="请输入内容" v-model="input" class="input-with-select">
                            <el-button slot="append" icon="el-icon-search" @click="search" type="primary"></el-button>
                        </el-input>
                    </el-col>
                    <el-drawer
                            title="搜索结果"
                            :visible.sync="drawer"
                    >
                        <!--信息-->
                        <el-row :span="24" style="overflow-y: hidden;">
                            <el-col :span="8" class="hb-box" v-for="(item,index) in mySQLData" :key="index">
                                <el-row :span="24">
                                    <el-col :span="24">
                                        <el-col :span="8" class="img-box" style="margin-left: 150px;padding-top: 15px">
                                            <a :href="item.official">
                                                <img :src="getImages(item.img)" alt="123">
                                            </a>
                                        </el-col>
                                    </el-col>
                                    <el-col :span="18" style="padding: 5px;margin: 15px 0 15px 80px;">
                                        <el-row :span="24" style="margin-bottom: 6px">
                                            <a :href="item.details">
                                                <el-col :span="18" class="name-box" style="white-space: nowrap;overflow: hidden;text-overflow: ellipsis;">{{ item.mname }}</el-col>
                                            </a>
                                            <el-col :span="4" class="year-box">{{ item.years }}</el-col>
                                        </el-row>
                                        <el-row :span="24" style="margin-bottom: 6px">
                                            <el-col class="db-box">
                                                <a href="">豆瓣
                                                    <span>{{ item.score }}</span>
                                                </a>
                                            </el-col>
                                        </el-row>
                                        <el-row :span="24" style="margin-bottom: 6px">
                                            <el-col class="dyy-box">
                                                <span class="dy-box">语言：</span>
                                                <span class="dyname-box">{{ item.languages }}</span>
                                            </el-col>
                                        </el-row>
                                        <el-row :span="24" style="margin-bottom: 6px">
                                            <el-col class="dyy-box">
                                                <span class="dy-box">导演：</span>
                                                <span class="dyname-box">{{ item.director }}</span>
                                            </el-col>
                                        </el-row>
                                        <el-row :span="24" style="margin-bottom: 6px">
                                            <el-col class="dyy-box">
                                                <span class="dy-box">类型：</span>
                                                <span class="dyname-box">{{ item.mold }}</span>
                                            </el-col>
                                        </el-row>
                                        <el-row :span="24" style="margin-bottom: 6px;width: 280px!important;display: flex">
                                            <el-col class="dyy-box" style="width: 280px!important;">
                                                <el-col :span="3" style="width: 42px!important;">
                                                    <span class="dy-box">主演：</span>
                                                </el-col>
                                                <el-col :span="20" style="white-space: nowrap;overflow: hidden;text-overflow: ellipsis;">
                                                    <span class="dyname-box"  style="width: 200px!important;">{{ item.act }}12312313213123123123123123123123123123</span>
                                                </el-col>
                                            </el-col>
                                        </el-row>
                                    </el-col>
                                </el-row>
                            </el-col>
                        </el-row>
                    </el-drawer>

                    <!--登录-->
                    <el-col :span="2" style="margin: 0 20px 0 10px;font-size: 14px;cursor: pointer" v-show="this.$store.state.flag">
                        <router-link :to="{name:'login'}" tag="div">
                            登录
                        </router-link>
                    </el-col>

                    <el-col :span="2" style="font-size: 14px;cursor: pointer;height: 60px;margin-left: 20px" v-show="!this.$store.state.flag">
                        <div style="height: 60px">
                            <el-dropdown style="height: 60px!important;">
                                <div style="padding-top: 10px">
                                    <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
                                </div>
                                <el-dropdown-menu slot="dropdown">
                                    <div @click="think">
                                        <el-dropdown-item icon="el-icon-star-off">想看</el-dropdown-item>
                                    </div>
                                    <div @click="logout">
                                        <el-dropdown-item icon="el-icon-ship">退出登录</el-dropdown-item>
                                    </div>
                                </el-dropdown-menu>
                            </el-dropdown>
                        </div>
                    </el-col>
                </el-col>
            </el-col>
        </el-row>

    </div>
</template>

<script>
    // @ is an alias to /src
    // import HelloWorld from '@/components/HelloWorld.vue'

    export default {
        name: 'headers',
        components: {
            // HelloWorld
        },
        data(){
            return {
                activeIndex: '1',
                input:'',
                drawer: false,
                mySQLData:[],
            }
        },
        methods: {
            handleSelect() {
            },
            think(){
              this.$router.push('/collection');
            },
            logout(){
                this.$router.push("/login");
                window.localStorage.removeItem('token')
            },
            getImages( _url ){
                if( _url !== undefined ){
                    let _u = _url.substring( 7 );
                    return 'https://images.weserv.nl/?url=' + _u;
                }
            },
            search(){
                let data = {'mname':this.input}
                this.$axios.post('/api/search',data).then((res)=>{
                    if(res.data.msg==='ok'){
                        this.drawer = true;
                        this.mySQLData=res.data.data;
                    }else {
                        this.$message.error(res.data.data)
                    }
                })
            },
        },
    }
</script>
<style>
    .header-box{
        width: 100%;
        height: 100%;
    }
    .el-container{
        width: 100%;
        height: 100%;
    }
    .el-header{
        background-color: #e3ebec;
        color: #333;
        text-align: center;
        line-height: 60px;
    }
    .left-box{
        font-weight: 600;
        font-size: 24px;
    }
    .right-box{
        display: flex;
        justify-content: space-between;
    }
    .el-menu--horizontal{
        border: none!important;
    }
    .el-menu-item{
        padding: 0!important;
    }
    .el-input__inner{
        height: 32px!important;
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
    .el-drawer section{
        height: 400px;
        overflow: auto;
    }
</style>
