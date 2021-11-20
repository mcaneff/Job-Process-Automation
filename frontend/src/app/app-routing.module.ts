import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {AngularFireAuthGuard, redirectUnauthorizedTo,customClaims} from '@angular/fire/auth-guard'

import { CreateUserPageComponent } from './create-user-page/create-user-page.component';
import { pipe } from 'rxjs';



  const routes: Routes = [

  {path: '', component: CreateUserPageComponent, pathMatch: 'full'},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
