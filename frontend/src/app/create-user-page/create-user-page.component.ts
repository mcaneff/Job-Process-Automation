import { Component, OnInit } from '@angular/core';
import { TimetableService } from "../timetable.service";
import { FormGroup, FormControl, Validators, NgForm } from "@angular/forms";
import {AngularFireAuth} from '@angular/fire/auth'
import { NgForOf } from '@angular/common';
import { Router } from '@angular/router';
@Component({
  selector: 'app-create-user-page',
  templateUrl: './create-user-page.component.html',
  styleUrls: ['./create-user-page.component.css']
})
export class CreateUserPageComponent implements OnInit {
  form: FormGroup;
  selFile: null
  selFile2: null
  constructor(
    private afAuth: AngularFireAuth,
    private router: Router,
    private timetableService:TimetableService,
  ) { }

  ngOnInit(): void {
    this.form = new FormGroup({
      email: new FormControl(
        "",
        Validators.compose([Validators.required])
      ),
      fname: new FormControl(
        "",
        Validators.compose([Validators.required])
      ),
      lname: new FormControl(
        "",
        Validators.compose([Validators.required])
      ),
      phone: new FormControl(
        "",
        Validators.compose([Validators.required])
      ),
      position: new FormControl(
        "",
        Validators.compose([Validators.required])
      ),
      linkedin: new FormControl(
        "",
        Validators.compose([Validators.required])
      ),
      website: new FormControl(
        "",
        Validators.compose([Validators.required])
      ),
      github: new FormControl(
        "",
        Validators.compose([Validators.required])
      ),
      twitter: new FormControl(
        "",
        Validators.compose([Validators.required])
      ),
      location: new FormControl(
        "",
        Validators.compose([Validators.required])
      ),
      gDate: new FormControl(
        "",
        Validators.compose([Validators.required])
      ),
      gYear: new FormControl(
        "",
        Validators.compose([Validators.required])
      ),
      university: new FormControl(
        "",
        Validators.compose([Validators.required])
      )
  }) //A form for sign up. Validation of fields like email and password is done using firebase
  }
  onFileSel(event){
    this.selFile=event.target.files[0]
  }
  onFileSel2(event){
    this.selFile2=event.target.files[0]
  }
  async onButtonClicked(form: FormGroup){
    
    const item={
      fname: form.value.fname,
      lname: form.value.fname,
      email: form.value.email,
      phone: form.value.phone,
      position: form.value.position,
      linkedin: form.value.linkedin,
      website: form.value.website,
      github: form.value.github,
      twitter: form.value.twitter,
      location: form.value.location,
      gDate: form.value.gDate,
      gYear: form.value.gYear,
      university: form.value.university
    }
    const fd=new FormData()
    fd.append('file', this.selFile, 'resume.pdf')


    const fd2=new FormData()
    fd2.append('file', this.selFile2, 'cover.pdf')


    this.timetableService.postF(fd).subscribe((res)=>{
        
    })

      this.timetableService.createV(item).subscribe((res)=>{
        
      })
      

    
    }


  
  
  


}
