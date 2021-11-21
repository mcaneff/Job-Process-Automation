import { Component, OnInit } from '@angular/core';
import { TimetableService } from "../timetable.service";
import { FormGroup, FormControl, Validators, NgForm } from "@angular/forms";
import { AngularFireAuth } from '@angular/fire/auth'
import { NgForOf } from '@angular/common';
import { Router } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';
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
    private timetableService: TimetableService,
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
  onFileSel(event) {
    this.selFile = event.target.files[0]
  }
  onFileSel2(event) {
    this.selFile2 = event.target.files[0]
  }
  async onButtonClicked(form: FormGroup) {
    console.log(form)
    const fd = new FormData()


    const first_name = form.value.fname
    const last_name = form.value.fname
    const email = form.value.email
    const phone = form.value.phone
    const position = form.value.position
    const linkedin = form.value.linkedin
    const website = form.value.website
    const github = form.value.github
    const twitter = form.value.twitter
    const location = form.value.location
    const graduation_date = form.value.gDate
    const graduation_year = form.value.gYear
    const university = form.value.university

    fd.append('first_name', first_name)
    fd.append('last_name', last_name)
    fd.append('email', email)
    fd.append('phone', phone)
    fd.append('position', position)
    fd.append('linkedin', linkedin)
    fd.append('website', website)
    fd.append('github', github)
    fd.append('twitter', twitter)
    fd.append('location', location)
    fd.append('graduation_date', graduation_date)
    fd.append('graduation_year', graduation_year)
    fd.append('university', university)


    fd.append('resume', this.selFile, 'resume.pdf')


    // const fd2 = new FormData()
    fd.append('cover_letter', this.selFile2, 'cover.pdf')

    this.timetableService.postF(fd).subscribe((res) => {

    })

    this.timetableService.createV(fd).subscribe((res) => {

    })



  }







}
