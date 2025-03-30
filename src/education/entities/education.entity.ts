import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { HydratedDocument } from 'mongoose';

export type EducationDocument = HydratedDocument<Education>;

@Schema({ timestamps: true })
export class Education {
  @Prop({ required: true })
  degree: string;

  @Prop({ required: true })
  institution: string;

  @Prop({ required: true })
  startYear: string;

  @Prop({ required: true })
  endYear: string;

  @Prop()
  location: string;

  @Prop()
  description: string;
}

export const EducationSchema = SchemaFactory.createForClass(Education);
