<template>
    <ul>
        <VnoteItem v-for='(item,index) in getAllDatas' :data='item'></VnoteItem>
    </ul>
</template>
<script>
import VnoteItem from './VnoteItem';
export default {
    name:'Vnote',
    data(){
        return{}
    },
    components:{
        VnoteItem,
    },
    computed:{
        getAllDatas(){
            return this.$store.state.alllist;
        }
    },
}
</script>
<style>

</style>
