// Reusable quiz. Usage: <div id="quiz"></div> + <script type="application/json" id="quiz-data">[{"q":"..","options":[".."],"answer":0,"why":".."}]</script>
// "answer" is the index in the written order; options are shuffled on every page load.
(function(){
  const data=JSON.parse(document.getElementById('quiz-data').textContent);
  const root=document.getElementById('quiz');
  const shuffle=a=>{for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
  data.forEach((item,i)=>{
    const box=document.createElement('div');box.className='q';
    const p=document.createElement('p');p.textContent=(i+1)+'. '+item.q;box.appendChild(p);
    const why=document.createElement('div');why.className='why';
    shuffle(item.options.map((opt,j)=>({opt,right:j===item.answer}))).forEach(o=>{
      const b=document.createElement('button');b.textContent=o.opt;
      b.onclick=()=>{
        if(box.dataset.done)return;
        if(o.right){b.className='ok';box.dataset.done=1;why.textContent='Correct. '+item.why}
        else{b.className='bad';why.textContent='Not this one. Try again.'}
      };
      box.appendChild(b);
    });
    box.appendChild(why);root.appendChild(box);
  });
})();
