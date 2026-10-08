// Reusable quiz. Usage: <div id="quiz"></div> + <script type="application/json" id="quiz-data">[{"q":"..","options":[".."],"answer":0,"why":".."}]</script>
(function(){
  const data=JSON.parse(document.getElementById('quiz-data').textContent);
  const root=document.getElementById('quiz');
  data.forEach((item,i)=>{
    const box=document.createElement('div');box.className='q';
    const p=document.createElement('p');p.textContent=(i+1)+'. '+item.q;box.appendChild(p);
    const why=document.createElement('div');why.className='why';
    item.options.forEach((opt,j)=>{
      const b=document.createElement('button');b.textContent=opt;
      b.onclick=()=>{
        if(box.dataset.done)return;
        if(j===item.answer){b.className='ok';box.dataset.done=1;why.textContent='Correct. '+item.why}
        else{b.className='bad';why.textContent='Not this one. Try again.'}
      };
      box.appendChild(b);
    });
    box.appendChild(why);root.appendChild(box);
  });
})();
