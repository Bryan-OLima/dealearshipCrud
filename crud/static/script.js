(function(win,doc){
    'use strict';

    if(doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorAll('.btnDel');
        for(let i=0; i < btnDel.length; i++){
            btnDel[i].addEventListener('click', function(event){
                if(confirm('Do you wanna remove this one?')){
                    return true, alert('Car removed');
                }else{
                    event.preventDefault(), alert('Car was not removed');
                }
            });
        }
    }

    if(doc.querySelector('.btnSave')){
        let btnSave = doc.querySelector('.btnSave');
            btnSave.addEventListener('click', function(event){
                    return true, alert('Done!');
            });
    }
})(window,document);