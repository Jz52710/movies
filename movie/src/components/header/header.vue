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
                    <el-col :span="12">
                        <el-input placeholder="请输入内容" v-model="input" class="input-with-select">
                        <el-button slot="append" icon="el-icon-search"></el-button>
                    </el-input>
                    </el-col>
                    <el-col :span="2" style="margin: 0 20px 0 10px;font-size: 14px;cursor: pointer">
                        <router-link :to="{name:'login'}" tag="div">
                            登录
                        </router-link>
                    </el-col>
                    <el-col :span="2" style="font-size: 14px;cursor: pointer">
                        <router-link :to="{name:'logon'}" tag="div">
                            注册
                        </router-link>
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
            }
        },
        methods: {
            handleSelect() {
            }
        }
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
</style>
